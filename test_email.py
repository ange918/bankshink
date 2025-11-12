#!/usr/bin/env python3
"""
Script de test pour vérifier la configuration SMTP
Ce script envoie un email de test pour confirmer que le système fonctionne correctement.
"""

from email_service import send_confirmation_email
import os

def test_smtp_configuration():
    print("🧪 Test de la configuration SMTP...")
    print(f"📧 SMTP Host: {os.getenv('SMTP_HOST', 'Non configuré')}")
    print(f"🔌 SMTP Port: {os.getenv('SMTP_PORT', 'Non configuré')}")
    print(f"👤 SMTP Username: {os.getenv('SMTP_USERNAME', 'Non configuré')}")
    print(f"✉️  From Email: {os.getenv('SMTP_FROM_EMAIL', 'Non configuré')}")
    print(f"📛 From Name: {os.getenv('SMTP_FROM_NAME', 'Non configuré')}")
    print("\n" + "="*60 + "\n")
    
    # Email de test
    test_email = os.getenv('SMTP_USERNAME', 'test@example.com')
    
    print(f"📨 Envoi d'un email de test à: {test_email}")
    
    # Données de test
    test_user_data = {
        'firstName': 'Jean',
        'lastName': 'Dupont',
        'loanAmount': '50000',
        'loanDuration': '120'
    }
    
    # Envoi de l'email en français
    success, message = send_confirmation_email(test_email, test_user_data, language='fr')
    
    print("\n" + "="*60 + "\n")
    
    if success:
        print("✅ EMAIL ENVOYÉ AVEC SUCCÈS!")
        print(f"📬 Message: {message}")
        print("\n💡 Vérifiez votre boîte de réception (et le dossier spam)")
    else:
        print("❌ ÉCHEC DE L'ENVOI D'EMAIL")
        print(f"⚠️  Erreur: {message}")
        print("\n🔧 Suggestions de dépannage:")
        print("   1. Vérifiez que le mot de passe d'application Gmail est correct")
        print("   2. Assurez-vous que la validation en 2 étapes est activée sur Gmail")
        print("   3. Vérifiez que l'adresse email SMTP_USERNAME est correcte")
        print("   4. Consultez CONFIGURATION_SMTP.md pour plus d'aide")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    test_smtp_configuration()
