#!/usr/bin/env python3
"""Translate SMTP messages in process_form.php to Dutch"""
import re

FR_TO_NL = {
    # Error messages
    "Méthode non autorisée": "Methode niet toegestaan",
    "Adresse email invalide": "Ongeldig e-mailadres",
    
    # Field labels
    "Prénom": "Voornaam",
    "Nom": "Naam",
    "Email": "Email",
    "Téléphone": "Telefoon",
    "Date de naissance": "Geboortedatum",
    "Type de crédit": "Type krediet",
    "Montant": "Bedrag",
    "Durée": "Looptijd",
    "Mensualité": "Maandelijkse betaling",
    "Message": "Bericht",
    
    # Email subject lines
    "Nouvelle demande depuis le site Shine Banque": "Nieuwe aanvraag vanaf de Shine Bank website",
    "Confirmation de votre demande - Shine Banque": "Bevestiging van uw aanvraag - Shine Bank",
    
    # Email body content
    "Shine Banque": "Shine Bank",
    "Nouvelle demande reçue": "Nieuwe aanvraag ontvangen",
    "Pièces jointes :": "Bijlagen:",
    "champ:": "veld:",
    "Erreur lors de l'envoi à l'administrateur:": "Fout bij verzenden naar beheerder:",
    "Erreur lors de l'envoi de la confirmation:": "Fout bij verzenden van bevestiging:",
    "Erreur lors de l'envoi:": "Fout bij verzenden:",
    
    # Confirmation email content
    'lang="fr"': 'lang="nl"',
    "Confirmation de votre demande": "Bevestiging van uw aanvraag",
    "✅ Votre demande a bien été reçue par": "✅ Uw aanvraag is goed ontvangen door",
    "Vous recevrez une réponse dans un délai de": "U ontvangt een antwoord binnen",
    "3 jours ouvrables": "3 werkdagen",
    "Merci de votre confiance.": "Dank u voor uw vertrouwen.",
    "© 2025 Shine Banque – Tous droits réservés.": "© 2025 Shine Bank – Alle rechten voorbehouden.",
    
    # Success message
    "Votre demande a bien été envoyée. Vous recevrez un mail de confirmation dans quelques instants.": "Uw aanvraag is succesvol verzonden. U ontvangt binnen enkele ogenblikken een bevestigingsmail."
}

def translate_php(content):
    """Apply Dutch translations to PHP content"""
    for fr, nl in FR_TO_NL.items():
        content = content.replace(fr, nl)
    return content

def main():
    import os
    files = ['process_form.php', 'PACKAGE_HEBERGEUR/process_form.php']
    
    for filepath in files:
        if not os.path.exists(filepath):
            print(f"  ⚠ Skipped: {filepath}")
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        translated = translate_php(content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(translated)
        
        print(f"  ✓ Translated: {filepath}")
    
    print("SMTP messages translated to Dutch!")

if __name__ == "__main__":
    main()
