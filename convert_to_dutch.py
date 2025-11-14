#!/usr/bin/env python3
"""
Script to remove multilingual scaffolding from Shine BK website HTML files.
Processes credit pages to remove:
- translations.js script tag
- language selector
- data-translate attributes
- Sets lang="nl"
"""

import re
import os
from pathlib import Path

CREDIT_PAGES = [
    "credit-consommation.html",
    "credit-express.html",
    "credit-immobilier.html",
    "credit-agricole.html",
    "credit-digital.html",
    "credit-automobile.html",
    "micro-credit.html",
    "credit-etudiant.html",
]

DIRECTORIES = [
    "pages",
    "PACKAGE_HEBERGEUR/pages"
]

def clean_multilingual_scaffolding(html_content):
    """Remove all multilingual infrastructure from HTML content."""
    
    html_content = re.sub(r'<html lang="[^"]*">', '<html lang="nl">', html_content)
    
    html_content = re.sub(
        r'\s*<script src="\.\./js/translations\.js"></script>\s*\n',
        '',
        html_content
    )
    
    lang_selector_pattern = r'\s*<div class="lang-selector">.*?</div>\s*\n'
    html_content = re.sub(lang_selector_pattern, '', html_content, flags=re.DOTALL)
    
    html_content = re.sub(r'\s+data-translate-phone', '', html_content)
    html_content = re.sub(r'\s+data-translate="[^"]*"', '', html_content)
    
    return html_content

def process_file(filepath):
    """Process a single HTML file to remove multilingual scaffolding."""
    print(f"Processing: {filepath}")
    
    if not os.path.exists(filepath):
        print(f"  ⚠ File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cleaned_content = clean_multilingual_scaffolding(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"  ✓ Cleaned successfully")
    return True

def main():
    """Main execution function."""
    print("=" * 60)
    print("Shine BK - Multilingual Scaffolding Removal")
    print("=" * 60)
    print()
    
    processed = 0
    skipped = 0
    
    for directory in DIRECTORIES:
        print(f"\nProcessing directory: {directory}/")
        print("-" * 60)
        
        for page in CREDIT_PAGES:
            filepath = os.path.join(directory, page)
            if process_file(filepath):
                processed += 1
            else:
                skipped += 1
    
    print()
    print("=" * 60)
    print(f"Summary: {processed} files processed, {skipped} skipped")
    print("=" * 60)
    print()
    print("Next step: Manually apply Dutch translations to cleaned files")

if __name__ == "__main__":
    main()
