#!/usr/bin/env python3
"""Fix corrupted HTML from over-aggressive translation"""
import os
import glob

# Critical HTML/attribute fixes
FIXES = [
    ('ljaarg=', 'lang='),
    ('<spjaar>', '<span>'),
    ('</spjaar>', '</span>'),
    ('<spjaar ', '<span '),
    ('ajaarbiedingen', 'aanbiedingen'),
    ('Vjaar ', 'Van '),
    ('vjaar ', 'van '),
    ('djaar ', 'dan '),
    ('Djaar ', 'Dan '),
    ('hjaar', 'han'),
    ('Hjaar', 'Han'),
    ('bjaar', 'ban'),
    ('Bjaar', 'Ban'),
    ('pjaar', 'pan'),
    ('Pjaar', 'Pan'),
    ('tjaar', 'tan'),
    ('Tjaar', 'Tan'),
    ('fjaar', 'fan'),
    ('Fjaar', 'Fan'),
    ('gjaar', 'gan'),
    ('Gjaar', 'Gan'),
    ('kjaar', 'kan'),
    ('Kjaar', 'Kan'),
    ('mjaar', 'man'),
    ('Mjaar', 'Man'),
    ('njaar', 'nan'),
    ('Njaar', 'Nan'),
    ('rjaar', 'ran'),
    ('Rjaar', 'Ran'),
    ('sjaar', 'san'),
    ('Sjaar', 'San'),
    ('wjaar', 'wan'),
    ('Wjaar', 'Wan'),
    ('zjaar', 'zan'),
    ('Zjaar', 'Zan'),
    ('jaarde', 'aarde'),
    ('Jaarde', 'Aarde'),
    ('finjaarcier', 'financier'),
    ('Finjaarcier', 'Financier'),
    ('Bjaark', 'Bank'),
    ('bjaark', 'bank'),
    ('demjaarde', 'demande'),
    ('jaarce', 'ance'),
    ('jaars', 'ans'),
    ('Jaars', 'Ans'),
    ('avjaart', 'avant'),
    ('Avjaart', 'Avant'),
    ('naissjaarce', 'naissance'),
]

def fix_file(filepath):
    """Fix corrupted HTML in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        for bad, good in FIXES:
            content = content.replace(bad, good)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"  ⚠ Error fixing {filepath}: {e}")
        return False

def main():
    print("=" * 60)
    print("Fixing Corrupted HTML from Translation")
    print("=" * 60)
    print()
    
    # Fix all HTML files in both directories
    patterns = [
        'index.html',
        'pages/*.html',
        'PACKAGE_HEBERGEUR/index.html',
        'PACKAGE_HEBERGEUR/pages/*.html'
    ]
    
    fixed_count = 0
    for pattern in patterns:
        for filepath in glob.glob(pattern):
            if fix_file(filepath):
                print(f"  ✓ Fixed: {filepath}")
                fixed_count += 1
    
    print()
    print("=" * 60)
    print(f"Fixed {fixed_count} corrupted files")
    print("=" * 60)

if __name__ == "__main__":
    main()
