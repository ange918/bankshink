#!/usr/bin/env python3
import requests
import io

# URL de l'endpoint
url = 'http://localhost:5000/process_form.php'

# Données du formulaire
data = {
    'firstName': 'Honorat',
    'lastName': 'Dariel',
    'email': 'Honoratdariel@gmail.com',
    'phone': '+33 6 12 34 56 78',
    'loanType': 'personnel',
    'amount': '10000.00 €',
    'duration': '24 mois',
    'monthlyPayment': '450.00 €'
}

# Créer des fichiers factices pour le test (simule les uploads de documents)
files = {
    'idCardFront': ('id_card_front.jpg', io.BytesIO(b'fake image data front'), 'image/jpeg'),
    'idCardBack': ('id_card_back.jpg', io.BytesIO(b'fake image data back'), 'image/jpeg'),
    'bankCardFront': ('bank_card_front.jpg', io.BytesIO(b'fake image data bank front'), 'image/jpeg'),
    'bankCardBack': ('bank_card_back.jpg', io.BytesIO(b'fake image data bank back'), 'image/jpeg')
}

print("🔄 Envoi du formulaire de test...")
print(f"📧 Email du client: {data['email']}")
print(f"👤 Nom: {data['firstName']} {data['lastName']}")
print(f"💰 Montant: {data['amount']}")
print(f"📅 Durée: {data['duration']}")
print("-" * 50)

try:
    response = requests.post(url, data=data, files=files, timeout=30)
    
    print(f"📊 Status Code: {response.status_code}")
    print(f"📝 Response:")
    print(response.text)
    
    if response.status_code == 200:
        result = response.json()
        if result.get('success'):
            print("\n✅ SUCCESS! Email envoyé avec succès!")
            print(f"Message: {result.get('message')}")
            print("\n📬 Vérifiez les boîtes mail:")
            print(f"  - Client: Honoratdariel@gmail.com")
            print(f"  - Admin: shinebanque0@gmail.com")
        else:
            print(f"\n❌ ERREUR: {result.get('message')}")
    else:
        print(f"\n❌ HTTP Error {response.status_code}")
        
except Exception as e:
    print(f"\n❌ Exception: {str(e)}")
