#!/usr/bin/env python3

import os
import sys
import argparse
import google.generativeai as genai
from typing import Optional
from modules.template_processor import process_template, parse_replacements

def setup_gemini() -> genai.GenerativeModel:
    """Initialize Gemini AI with API key from environment."""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro')

def call_gemini(prompt: str, model: Optional[str] = None) -> str:
    """Call Gemini AI with the given prompt."""
    try:
        if model:
            gemini_model = genai.GenerativeModel(model)
        else:
            gemini_model = setup_gemini()
        
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description='Call Gemini AI with a prompt')
    parser.add_argument('prompt', nargs='?', help='The prompt to send to Gemini (or read from stdin if not provided)')
    parser.add_argument('--model', '-m', default='gemini-2.0-flash-lite', 
                       help='Gemini model to use (default: gemini-2.0-flash-lite)')
    parser.add_argument('--file', '-f', help='Read prompt from file instead')
    parser.add_argument('--replace', action='append', default=[], 
                       help='Template replacements in key=value format (can be used multiple times)')
    
    args = parser.parse_args()
    
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                prompt = f.read().strip()
        except FileNotFoundError:
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
            # Use script's directory as base path for relative file paths
            script_dir = os.path.dirname(os.path.abspath(__file__))
            replacements = parse_replacements(args.replace, script_dir)
            prompt = process_template(prompt, replacements, script_dir)
        except ValueError as e:
            print(f"Template processing error: {e}", file=sys.stderr)
            sys.exit(1)
    
    response = call_gemini(prompt, args.model)
    print(response)

if __name__ == '__main__':
    main()