#!/usr/bin/env python3
"""
Simple script to clean up NLI Dataset using file_name parameter in JSON files.
Matches JSON files with TXT files and removes duplicates.
"""

import os
import json
import shutil
from collections import defaultdict

def extract_filename_from_json(json_path):
    """Extract the file_name parameter from a JSON file."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Handle different JSON structures
            if isinstance(data, dict):
                return data.get('file_name', None)
            elif isinstance(data, list) and len(data) > 0:
                # If it's a list, check the first item
                first_item = data[0]
                if isinstance(first_item, dict):
                    return first_item.get('file_name', None)
            return None
    except Exception as e:
        print(f"Error reading {json_path}: {e}")
        return None

def normalize_filename(filename):
    """Normalize filename for matching."""
    if filename:
        # Remove .snippet suffix if present
        if filename.endswith('.snippet'):
            filename = filename[:-8]
        # Remove .txt suffix if present
        if filename.endswith('.txt'):
            filename = filename[:-4]
        return filename
    return None

def main():
    print("Starting NLI Dataset cleanup...")
    
    # Find all JSON files
    json_files = []
    for root, dirs, files in os.walk('.'):
        if 'backup_before_cleanup' in root:
            continue
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    
    print(f"Found {len(json_files)} JSON files")
    
    # Find all TXT files
    txt_files = []
    for root, dirs, files in os.walk('.'):
        if 'backup_before_cleanup' in root:
            continue
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    
    print(f"Found {len(txt_files)} TXT files")
    
    # Extract filenames from JSONs
    json_filename_map = {}
    for json_path in json_files:
        filename = extract_filename_from_json(json_path)
        if filename:
            normalized = normalize_filename(filename)
            if normalized:
                json_filename_map[json_path] = normalized
    
    print(f"Extracted filenames from {len(json_filename_map)} JSON files")
    
    # Create TXT filename map
    txt_filename_map = {}
    for txt_path in txt_files:
        filename = os.path.basename(txt_path)
        normalized = normalize_filename(filename)
        if normalized:
            txt_filename_map[normalized] = txt_path
    
    print(f"Mapped {len(txt_filename_map)} TXT files")
    
    # Find matches
    matches = []
    unmatched_jsons = []
    unmatched_txts = set(txt_filename_map.keys())
    
    for json_path, json_filename in json_filename_map.items():
        if json_filename in txt_filename_map:
            matches.append((json_path, txt_filename_map[json_filename]))
            unmatched_txts.discard(json_filename)
        else:
            unmatched_jsons.append(json_path)
    
    print(f"Found {len(matches)} matching pairs")
    print(f"Unmatched JSONs: {len(unmatched_jsons)}")
    print(f"Unmatched TXTs: {len(unmatched_txts)}")
    
    # Create backup directory
    backup_dir = "backup_duplicates"
    os.makedirs(backup_dir, exist_ok=True)
    
    # Remove duplicate JSONs (keep one per filename)
    filename_to_keep = {}
    duplicates_removed = 0
    
    for json_path, json_filename in json_filename_map.items():
        if json_filename in filename_to_keep:
            # This is a duplicate, move to backup
            backup_path = os.path.join(backup_dir, os.path.basename(json_path))
            shutil.move(json_path, backup_path)
            duplicates_removed += 1
        else:
            filename_to_keep[json_filename] = json_path
    
    print(f"Removed {duplicates_removed} duplicate JSON files")
    
    # Final count
    remaining_jsons = len([f for f in os.listdir('.') if f.endswith('.json')])
    remaining_txts = len([f for f in os.listdir('.') if f.endswith('.txt')])
    
    print(f"\nFinal counts:")
    print(f"JSON files: {remaining_jsons}")
    print(f"TXT files: {remaining_txts}")

if __name__ == "__main__":
    main() 