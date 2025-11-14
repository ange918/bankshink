#!/usr/bin/env python3
"""Final Dutch translation - using complete phrase replacements to avoid HTML corruption"""
import os
import glob

# Complete phrase translations - no risk of HTML corruption
TRANSLATIONS = [
    # About section - index.html
    ("Shine Bank est votre partenaire financier de confiance depuis plus de 15 ans. Notre mission est de rendre les services bancaires accessibles, transparents et adaptés à vos besoins.",
     "Shine Bank is al meer dan 15 jaar uw vertrouwde financiële partner. Onze missie is om bankdiensten toegankelijk, transparant en afgestemd op uw behoeften te maken."),
    
    # Any remaining French labels/headers
    ("Votre partenaire financier", "Uw financiële partner"),
    ("Notre mission", "Onze missie"),
    ("Nous sommes", "Wij zijn"),
    ("Téléphone", "Telefoon"),
    ("Adresse", "Adres"),
    ("Horaires d'ouverture", "Openingstijden"),
    ("Horaires", "Openingstijden"),
    
    # Common French phrases
    ("Bienvenue", "Welkom"),
    ("Plus d'informations", "Meer informatie"),
]

def translate_file(filepath):
    """Apply final Dutch translations"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        for fr, nl in TRANSLATIONS:
            content = content.replace(fr, nl)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"  ⚠ Error: {filepath}: {e}")
        return False

def main():
    print("Applying final Dutch translations...")
    
    patterns = [
        'index.html',
        'pages/*.html',
        'PACKAGE_HEBERGEUR/index.html',
        'PACKAGE_HEBERGEUR/pages/*.html'
    ]
    
    count = 0
    for pattern in patterns:
        for filepath in glob.glob(pattern):
            if translate_file(filepath):
                print(f"  ✓ Translated: {filepath}")
                count += 1
    
    print(f"\nFinal translations applied to {count} files!")

if __name__ == "__main__":
    main()
