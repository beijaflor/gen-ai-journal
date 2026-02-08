#!/usr/bin/env python3

import os
import sys
import argparse
import re
import logging
import requests
import json
from datetime import datetime, timezone
from bs4 import BeautifulSoup
import google.generativeai as genai
from typing import Optional, Dict, Any, Tuple
from modules.template_processor import process_template, parse_replacements

def fetch_url_content(url: str, timeout: int = 30) -> str:
    """Fetch content from a URL and extract readable text."""
    try:
        logging.info(f"Fetching content from URL: {url}")
        
        # Set proper headers to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        
        logging.info(f"Successfully fetched {len(response.content)} bytes from URL")
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Extract text content
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        logging.info(f"Extracted {len(text)} characters of text content")
        return text
        
    except requests.exceptions.RequestException as e:
        error_msg = f"Error fetching URL {url}: {str(e)}"
        logging.error(error_msg)
        return f"[ERROR: {error_msg}]"
    except Exception as e:
        error_msg = f"Error processing content from {url}: {str(e)}"
        logging.error(error_msg)
        return f"[ERROR: {error_msg}]"

def setup_gemini() -> genai.GenerativeModel:
    """Initialize Gemini AI with API key from environment."""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro')

def clean_gemini_output(text: str) -> str:
    """Clean Gemini output by removing debug info and extracting summary content."""
    lines = text.split('\n')
    cleaned_lines = []
    
    # Find start of actual content (after ## heading)
    content_started = False
    for line in lines:
        # Skip debug/metadata lines
        if any(pattern in line for pattern in [
            '[WebFetchTool]',
            'Loaded cached credentials.',
            'using macos seatbelt',
            'node:',
            'Error fetching'
        ]):
            continue
        
        # Start including content from ## headings
        if line.startswith('## '):
            content_started = True
        
        if content_started:
            # Stop at JSON output or similar structured data
            if line.strip() in ['{', '}'] or line.startswith('```json'):
                break
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines).strip()

def validate_json_summary(data: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """Validate JSON summary structure against v1.0 schema.

    Returns:
        (success: bool, error_message: Optional[str])
    """
    try:
        # Check required top-level fields
        if 'metadata' not in data or 'content' not in data:
            return False, "Missing required top-level fields: metadata or content"

        metadata = data['metadata']
        content = data['content']

        # Validate metadata
        if metadata.get('version') != '1.0':
            return False, f"Invalid version: {metadata.get('version')}, expected '1.0'"

        if not metadata.get('generatedAt'):
            return False, "Missing generatedAt in metadata"

        if not metadata.get('generatedBy'):
            return False, "Missing generatedBy in metadata"

        # Validate content required fields
        required_content_fields = [
            'title', 'url', 'language', 'contentType',
            'oneSentenceSummary', 'summaryBody', 'topics', 'scores'
        ]

        for field in required_content_fields:
            if field not in content:
                return False, f"Missing required content field: {field}"

        # Validate scores structure
        scores = content['scores']
        required_score_fields = [
            'signal', 'depth', 'uniqueness', 'practical', 'antiHype',
            'mainJournal', 'annexPotential', 'overall'
        ]

        for field in required_score_fields:
            if field not in scores:
                return False, f"Missing required score field: {field}"

        # Validate score ranges
        dimension_scores = [
            scores['signal'], scores['depth'], scores['uniqueness'],
            scores['practical'], scores['antiHype']
        ]

        for score in dimension_scores:
            if not isinstance(score, int) or score < 0 or score > 5:
                return False, f"Dimension score out of range (0-5): {score}"

        composite_scores = [
            scores['mainJournal'], scores['annexPotential'], scores['overall']
        ]

        for score in composite_scores:
            if not isinstance(score, int) or score < 0 or score > 100:
                return False, f"Composite score out of range (0-100): {score}"

        # Validate topics array
        topics = content['topics']
        if not isinstance(topics, list):
            return False, "Topics must be an array"

        if len(topics) < 1 or len(topics) > 5:
            return False, f"Topics array must have 1-5 elements, got {len(topics)}"

        # Validate string lengths
        if len(content['title']) < 1 or len(content['title']) > 200:
            return False, f"Title length out of range (1-200): {len(content['title'])}"

        if len(content['oneSentenceSummary']) < 10 or len(content['oneSentenceSummary']) > 300:
            return False, f"One sentence summary length out of range (10-300): {len(content['oneSentenceSummary'])}"

        if len(content['summaryBody']) < 100 or len(content['summaryBody']) > 1200:
            return False, f"Summary body length out of range (100-1200): {len(content['summaryBody'])}"

        return True, None

    except Exception as e:
        return False, f"Validation error: {str(e)}"


def get_gemini_schema():
    """Get Gemini-compatible schema for structured output.

    Converts our JSON schema to Gemini's schema format using their Type system.
    Based on: https://ai.google.dev/gemini-api/docs/structured-output
    """
    from google.ai.generativelanguage_v1beta.types import Schema, Type

    return Schema(
        type=Type.OBJECT,
        required=["metadata", "content"],
        properties={
            "metadata": Schema(
                type=Type.OBJECT,
                required=["version", "generatedAt", "generatedBy"],
                properties={
                    "version": Schema(
                        type=Type.STRING,
                        description="Schema version (always '1.0')"
                    ),
                    "generatedAt": Schema(
                        type=Type.STRING,
                        description="ISO 8601 timestamp of generation"
                    ),
                    "generatedBy": Schema(
                        type=Type.STRING,
                        description="Model identifier (e.g., gemini-3-flash-preview)"
                    )
                }
            ),
            "content": Schema(
                type=Type.OBJECT,
                required=[
                    "title", "url", "language", "contentType",
                    "oneSentenceSummary", "summaryBody", "topics", "scores"
                ],
                properties={
                    "title": Schema(
                        type=Type.STRING,
                        description="Article title in Japanese (1-200 chars)"
                    ),
                    "originalTitle": Schema(
                        type=Type.STRING,
                        description="Original title if article is in non-Japanese language",
                        nullable=True
                    ),
                    "url": Schema(
                        type=Type.STRING,
                        description="Article URL"
                    ),
                    "language": Schema(
                        type=Type.STRING,
                        enum=["ja", "en", "zh", "ko", "other"],
                        description="Article language code"
                    ),
                    "contentType": Schema(
                        type=Type.STRING,
                        enum=[
                            "🚀 Product Launch (製品発表)",
                            "🔬 Research & Analysis (研究・分析)",
                            "💡 Tutorial & How-to (チュートリアル)",
                            "🎯 Opinion & Commentary (意見・論評)",
                            "📊 Industry News (業界ニュース)",
                            "🛠️ Tools & Resources (ツール・リソース)",
                            "🎓 Learning & Education (学習・教育)",
                            "🌐 Community & Events (コミュニティ・イベント)"
                        ],
                        description="Content category"
                    ),
                    "oneSentenceSummary": Schema(
                        type=Type.STRING,
                        description="One sentence summary in Japanese (10-300 chars)"
                    ),
                    "summaryBody": Schema(
                        type=Type.STRING,
                        description="Full summary body in markdown format (100-1200 chars)"
                    ),
                    "topics": Schema(
                        type=Type.ARRAY,
                        description="Topic tags (1-5 tags)",
                        items=Schema(
                            type=Type.STRING,
                            description="Topic tag (1-50 chars)"
                        )
                    ),
                    "scores": Schema(
                        type=Type.OBJECT,
                        required=[
                            "signal", "depth", "uniqueness", "practical", "antiHype",
                            "mainJournal", "annexPotential", "overall"
                        ],
                        properties={
                            "signal": Schema(
                                type=Type.INTEGER,
                                description="Signal-to-noise ratio (0-5)"
                            ),
                            "depth": Schema(
                                type=Type.INTEGER,
                                description="Content depth (0-5)"
                            ),
                            "uniqueness": Schema(
                                type=Type.INTEGER,
                                description="Perspective uniqueness (0-5)"
                            ),
                            "practical": Schema(
                                type=Type.INTEGER,
                                description="Practical applicability (0-5)"
                            ),
                            "antiHype": Schema(
                                type=Type.INTEGER,
                                description="Anti-hype factor (0-5)"
                            ),
                            "mainJournal": Schema(
                                type=Type.INTEGER,
                                description="Main journal fit score (0-100)"
                            ),
                            "annexPotential": Schema(
                                type=Type.INTEGER,
                                description="Annex journal potential score (0-100)"
                            ),
                            "overall": Schema(
                                type=Type.INTEGER,
                                description="Overall quality score (0-100)"
                            )
                        }
                    )
                }
            )
        }
    )


def call_gemini_structured(prompt: str, model: Optional[str] = None) -> Dict[str, Any]:
    """Call Gemini AI with structured output using native schema support.

    Args:
        prompt: The prompt to send
        model: Model name to use

    Returns:
        Parsed JSON response matching v1.0 schema
    """
    try:
        logging.info(f"Using model: {model or 'gemini-pro'} with native structured output")
        logging.info(f"Prompt length: {len(prompt)} characters")
        logging.debug(f"Full prompt:\n{'-'*50}\n{prompt}\n{'-'*50}")

        # Get Gemini schema
        schema = get_gemini_schema()
        logging.info("Using native Gemini schema for structured output")

        # Create model with schema configuration
        gemini_model = genai.GenerativeModel(
            model_name=model or 'gemini-pro',
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema=schema
            )
        )

        logging.info("Sending structured output request to Gemini...")

        response = gemini_model.generate_content(prompt)

        logging.info("Received response from Gemini")

        # Parse JSON response
        result_text = response.text
        logging.info(f"Response length: {len(result_text)} characters")
        logging.debug(f"Raw response:\n{'-'*50}\n{result_text}\n{'-'*50}")

        # Parse JSON
        result_data = json.loads(result_text)

        # Gemini's structured output should already match our schema,
        # but we still add/verify metadata fields for consistency
        if 'metadata' not in result_data:
            result_data['metadata'] = {}

        result_data['metadata']['version'] = '1.0'
        result_data['metadata']['generatedAt'] = datetime.now(timezone.utc).isoformat()
        result_data['metadata']['generatedBy'] = model or 'gemini-pro'

        return result_data

    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse JSON response: {str(e)}")
        logging.error(f"Response text: {result_text[:1000]}")
        raise ValueError(f"Invalid JSON response from Gemini: {str(e)}")
    except Exception as e:
        logging.error(f"Error calling Gemini with structured output: {str(e)}")
        raise


def call_gemini(prompt: str, model: Optional[str] = None, clean_output: bool = False, disable_cache: bool = False, enable_context_cache: bool = False, static_content: Optional[str] = None) -> str:
    """Call Gemini AI with the given prompt.

    Args:
        prompt: The full prompt or dynamic content to send
        model: Model name to use
        clean_output: Whether to clean the output
        disable_cache: Disable implicit caching
        enable_context_cache: Enable explicit context caching (for repeated static content)
        static_content: Static content to cache (used with enable_context_cache)
    """
    try:
        logging.info(f"Using model: {model or 'gemini-pro'}")
        logging.info(f"Prompt length: {len(prompt)} characters")
        logging.debug(f"Full prompt:\n{'-'*50}\n{prompt}\n{'-'*50}")

        if model:
            gemini_model = genai.GenerativeModel(model)
        else:
            gemini_model = setup_gemini()

        logging.info("Sending request to Gemini...")

        # Configure generation parameters
        generation_config = {}

        # Handle explicit context caching
        if enable_context_cache and static_content and not disable_cache:
            try:
                logging.info("Using explicit context caching")
                logging.info(f"Static content size: {len(static_content)} characters")

                # Create cached content with static part
                import datetime
                cache = genai.caching.CachedContent.create(
                    model=model or 'gemini-pro',
                    contents=[static_content],
                    ttl=datetime.timedelta(hours=1),  # Cache for 1 hour (enough for batch processing)
                )
                logging.info(f"Created cache with name: {cache.name}")

                # Use the cached model for generation
                cached_model = genai.GenerativeModel.from_cached_content(cache)
                response = cached_model.generate_content(prompt)

                # Clean up cache after use
                cache.delete()
                logging.info("Cache deleted after use")

            except Exception as cache_error:
                logging.warning(f"Context caching failed, falling back to normal mode: {cache_error}")
                # Fall back to normal generation
                response = gemini_model.generate_content(prompt)
        else:
            # Normal generation (with implicit caching if not disabled)
            if disable_cache:
                logging.info("Context caching disabled")
                generation_config['cached_content'] = None

            response = gemini_model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(**generation_config) if generation_config else None
            )

        logging.info("Received response from Gemini")

        result = response.text
        logging.info(f"Response length: {len(result)} characters")

        if clean_output:
            logging.info("Cleaning output...")
            original_length = len(result)
            result = clean_gemini_output(result)
            logging.info(f"Cleaned output: {original_length} -> {len(result)} characters")

        return result
    except Exception as e:
        logging.error(f"Error calling Gemini: {str(e)}")
        return f"Error calling Gemini: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description='Call Gemini AI with a prompt')
    parser.add_argument('prompt', nargs='?', help='The prompt to send to Gemini (or read from stdin if not provided)')
    parser.add_argument('--model', '-m', default='gemini-2.5-flash-lite',
                       help='Gemini model to use (default: gemini-2.5-flash-lite)')
    parser.add_argument('--file', '-f', help='Read prompt from file instead')
    parser.add_argument('--replace', action='append', default=[], 
                       help='Template replacements in key=value format (can be used multiple times)')
    parser.add_argument('--url', '-u', help='Summarize a URL using the summarize.prompt template')
    parser.add_argument('--clean', '-c', action='store_true', 
                       help='Clean output by removing debug info and extracting content')
    parser.add_argument('--debug', '-d', action='store_true',
                       help='Enable debug logging')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    parser.add_argument('--no-cache', action='store_true',
                       help='Disable context caching for this request')
    parser.add_argument('--enable-context-cache', action='store_true', default=True,
                       help='Enable explicit context caching (caches static prompt content for cost savings, enabled by default)')
    parser.add_argument('--disable-context-cache', action='store_true',
                       help='Disable explicit context caching')
    parser.add_argument('--output', '-o', help='Output file path (if not specified, output to stdout)')
    parser.add_argument('--format', choices=['markdown', 'json'], default='markdown',
                       help='Output format: markdown (default) or json (structured output with native Gemini schema)')

    args = parser.parse_args()

    # Get script directory (needed for relative paths)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Setup logging
    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format='[DEBUG] %(message)s', stream=sys.stderr)
    elif args.verbose:
        logging.basicConfig(level=logging.INFO, format='[INFO] %(message)s', stream=sys.stderr)
    else:
        logging.basicConfig(level=logging.WARNING, stream=sys.stderr)
    
    # Handle URL summarization
    if args.url:
        logging.info(f"URL summarization mode for: {args.url} (format: {args.format})")

        # Use JSON prompt for JSON format, markdown prompt for markdown format
        if args.format == 'json':
            prompt_file = os.path.join(script_dir, '..', 'prompts', 'summarize-json.prompt')
        else:
            prompt_file = os.path.join(script_dir, '..', 'prompts', 'summarize.prompt')

        logging.debug(f"Looking for prompt file: {prompt_file}")

        if not os.path.exists(prompt_file):
            logging.error(f"Prompt file not found: {prompt_file}")
            print(f"Error: {prompt_file} not found", file=sys.stderr)
            sys.exit(1)
        
        try:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                prompt = f.read().strip()
            logging.info(f"Loaded prompt template ({len(prompt)} chars)")
            
            # Replace {{url}} placeholder
            prompt = prompt.replace('{{url}}', args.url)
            
            # Process template for file inclusions
            try:
                logging.info("Processing template for file inclusions...")
                prompt = process_template(prompt, {}, script_dir, fetch_function=fetch_url_content)
                logging.debug(f"Prompt after template processing:\n{'-'*50}\n{prompt}\n{'-'*50}")
            except ValueError as e:
                logging.error(f"Template processing error: {e}")
                print(f"Template processing error: {e}", file=sys.stderr)
                sys.exit(1)
            
            logging.info(f"Final prompt length: {len(prompt)} characters")
            
            # args.clean = True  # Auto-enable cleaning for URL summarization
            args.model = 'gemini-3-flash-preview'  # Use latest model for URL summarization
            logging.info(f"Using model: {args.model} with clean output enabled")
            
        except FileNotFoundError:
            logging.error(f"Prompt file not found: {prompt_file}")
            print(f"Error: Prompt file '{prompt_file}' not found", file=sys.stderr)
            sys.exit(1)
    elif args.file:
        logging.info(f"Reading prompt from file: {args.file}")
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                prompt = f.read().strip()
            logging.info(f"Loaded prompt from file ({len(prompt)} chars)")
            logging.debug(f"File prompt content:\n{'-'*50}\n{prompt}\n{'-'*50}")
        except FileNotFoundError:
            logging.error(f"File not found: {args.file}")
            print(f"Error: File '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
    elif args.prompt:
        prompt = args.prompt
    else:
        # Read from stdin
        if sys.stdin.isatty():
            print("Error: No prompt provided and stdin is empty", file=sys.stderr)
            sys.exit(1)
        prompt = sys.stdin.read().strip()
    
    if not prompt:
        print("Error: No prompt provided", file=sys.stderr)
        sys.exit(1)
    
    # Process template if replacements are provided
    if args.replace:
        try:
            logging.info(f"Processing template with replacements: {args.replace}")
            # Use script's directory as base path for relative file paths
            replacements = parse_replacements(args.replace, script_dir)
            logging.debug(f"Parsed replacements: {replacements}")
            prompt = process_template(prompt, replacements, script_dir, fetch_function=fetch_url_content)
            logging.debug(f"Prompt after template processing:\n{'-'*50}\n{prompt}\n{'-'*50}")
        except ValueError as e:
            logging.error(f"Template processing error: {e}")
            print(f"Template processing error: {e}", file=sys.stderr)
            sys.exit(1)
    
    # Final debug log showing the complete prompt before API call
    logging.debug(f"Final prompt being sent to Gemini:\n{'-'*60}\n{prompt}\n{'-'*60}")

    # For URL mode with context caching enabled, separate static from dynamic content
    static_content = None
    dynamic_prompt = prompt

    # Determine if context caching should be enabled
    enable_caching = args.enable_context_cache and not args.disable_context_cache

    if enable_caching and args.url:
        # Split prompt into static (template) and dynamic (article) parts
        # The marker "# Article Content" indicates where dynamic content starts
        if "# Article Content" in prompt:
            parts = prompt.split("# Article Content", 1)
            static_content = parts[0].strip()
            dynamic_prompt = "# Article Content" + parts[1]
            logging.info(f"Context caching enabled: static={len(static_content)} chars, dynamic={len(dynamic_prompt)} chars")
        else:
            logging.warning("Could not find '# Article Content' marker, using full prompt without caching")
    elif args.disable_context_cache:
        logging.info("Context caching explicitly disabled")

    # Handle structured JSON output or regular text output
    if args.format == 'json':
        # Use native Gemini structured output with schema
        logging.info("JSON format: using native Gemini structured output")

        try:
            # Call Gemini with structured output
            response_data = call_gemini_structured(
                dynamic_prompt,
                args.model
            )

            # Validate JSON structure (safety check - Gemini should already match schema)
            logging.info("Validating JSON structure...")
            is_valid, error_msg = validate_json_summary(response_data)

            if not is_valid:
                logging.error(f"JSON validation failed: {error_msg}")
                print(f"Error: JSON validation failed: {error_msg}", file=sys.stderr)
                sys.exit(1)

            logging.info("JSON validation passed")

            # Convert to formatted JSON string
            response = json.dumps(response_data, ensure_ascii=False, indent=2)

        except Exception as e:
            logging.error(f"Failed to generate structured JSON: {e}")
            print(f"Error: Failed to generate structured JSON: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Regular markdown output
        response = call_gemini(
            dynamic_prompt,
            args.model,
            args.clean,
            args.no_cache,
            enable_context_cache=enable_caching,
            static_content=static_content
        )

    # Output to file or stdout
    if args.output:
        try:
            logging.info(f"Writing output to file: {args.output}")
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(response)
            logging.info(f"Successfully wrote {len(response)} characters to {args.output}")
        except IOError as e:
            logging.error(f"Error writing to file {args.output}: {str(e)}")
            print(f"Error writing to file {args.output}: {str(e)}", file=sys.stderr)
            sys.exit(1)
    else:
        print(response)

if __name__ == '__main__':
    main()