#!/usr/bin/env python3
"""Clean multilingual scaffolding from main pages"""
import re
import os

FILES = [
    "index.html",
    "pages/a-propos.html",
    "pages/contact.html",
    "pages/simulateur.html",
    "PACKAGE_HEBERGEUR/index.html",
    "PACKAGE_HEBERGEUR/pages/a-propos.html",
    "PACKAGE_HEBERGEUR/pages/contact.html",
    "PACKAGE_HEBERGEUR/pages/simulateur.html"
]

def clean_multilingual_scaffolding(html_content):
    """Remove all multilingual infrastructure from HTML content."""
    html_content = re.sub(r'<html lang="[^"]*">', '<html lang="nl">', html_content)
    html_content = re.sub(r'\s*<script src="(\.\.\/)?js/translations\.js"></script>\s*\n', '', html_content)
    lang_selector_pattern = r'\s*<div class="lang-selector">.*?</div>\s*\n'
    html_content = re.sub(lang_selector_pattern, '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'\s+data-translate-phone', '', html_content)
    html_content = re.sub(r'\s+data-translate="[^"]*"', '', html_content)
    return html_content

def main():
    print("Cleaning main pages...")
    for filepath in FILES:
        if not os.path.exists(filepath):
            print(f"  ⚠ Skipped: {filepath}")
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        cleaned = clean_multilingual_scaffolding(content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"  ✓ Cleaned: {filepath}")
    print("Done!")

if __name__ == "__main__":
    main()
