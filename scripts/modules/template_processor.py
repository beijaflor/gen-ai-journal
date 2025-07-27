import re
import os
from typing import Dict, Any


def process_template(text: str, replacements: Dict[str, Any], base_path: str = None, fetch_function=None) -> str:
    """
    Process template text with variable and file replacements.
    
    Supports:
    - {{variable}} - string replacement
    - {{file:path}} - file content inclusion (relative paths relative to base_path)
    - {{fetch:"URL"}} - fetch URL content (requires fetch_function)
    
    Args:
        text: Template text to process
        replacements: Dictionary of variable replacements
        base_path: Base directory for relative file paths (defaults to current working directory)
        fetch_function: Optional function to fetch URL content, signature: fetch_function(url: str) -> str
        
    Returns:
        Processed text with all substitutions made
        
    Raises:
        ValueError: If required variables are missing or files not found
    """
    processed_text = text
    
    # Phase 1: Replace variables {{variable}}
    variable_pattern = r'\{\{([^:}]+)\}\}'
    
    def replace_variable(match):
        var_name = match.group(1).strip()
        if var_name not in replacements:
            raise ValueError(f"Missing required variable: {var_name}")
        return str(replacements[var_name])
    
    processed_text = re.sub(variable_pattern, replace_variable, processed_text)
    
    # Phase 2: Replace file inclusions {{file:path}}
    file_pattern = r'\{\{file:([^}]+)\}\}'
    
    def replace_file(match):
        file_path = match.group(1).strip()
        
        # Resolve relative paths relative to base_path
        if base_path and not os.path.isabs(file_path):
            file_path = os.path.join(base_path, file_path)
        
        if not os.path.exists(file_path):
            raise ValueError(f"File not found: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise ValueError(f"Error reading file {file_path}: {str(e)}")
    
    processed_text = re.sub(file_pattern, replace_file, processed_text)
    
    # Phase 3: Replace URL fetch {{fetch:"URL"}}
    if fetch_function:
        fetch_pattern = r'\{\{fetch:"([^"]+)"\}\}'
        
        def replace_fetch(match):
            url = match.group(1).strip()
            try:
                return fetch_function(url)
            except Exception as e:
                raise ValueError(f"Error fetching URL {url}: {str(e)}")
        
        processed_text = re.sub(fetch_pattern, replace_fetch, processed_text)
    
    return processed_text


def parse_replacements(replace_args: list, base_path: str = None) -> Dict[str, str]:
    """
    Parse command line replacement arguments.
    
    Supports:
    - key=value - string replacement
    - key=@filename - file content replacement (relative to base_path)
    
    Args:
        replace_args: List of "key=value" strings
        base_path: Base directory for relative file paths (defaults to current working directory)
        
    Returns:
        Dictionary of key-value pairs
        
    Raises:
        ValueError: If argument format is invalid or file not found
    """
    replacements = {}
    
    for arg in replace_args:
        if '=' not in arg:
            raise ValueError(f"Invalid replacement format: {arg}. Expected key=value")
        
        key, value = arg.split('=', 1)
        if not key.strip():
            raise ValueError(f"Empty key in replacement: {arg}")
        
        key = key.strip()
        
        # Handle file content replacement (@filename)
        if value.startswith('@'):
            file_path = value[1:]  # Remove @ prefix
            
            # Resolve relative paths relative to base_path
            if base_path and not os.path.isabs(file_path):
                file_path = os.path.join(base_path, file_path)
            
            if not os.path.exists(file_path):
                raise ValueError(f"File not found for replacement '{key}': {file_path}")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    replacements[key] = f.read()
            except Exception as e:
                raise ValueError(f"Error reading file {file_path} for replacement '{key}': {str(e)}")
        else:
            replacements[key] = value
    
    return replacements