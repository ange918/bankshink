# Configuration SMTP pour l'envoi d'emails

## Étapes de configuration

### 1. Créer le fichier .env

Copiez le fichier `.env.example` et renommez-le en `.env` :

```bash
cp .env.example .env
```

### 2. Configuration Gmail

Pour utiliser Gmail avec SMTP, vous devez créer un **mot de passe d'application** :

#### Étapes pour créer un mot de passe d'application Gmail :

1. Connectez-vous à votre compte Gmail (shinebanque0@gmail.com)
2. Allez sur https://myaccount.google.com/security
3. Activez la validation en 2 étapes si ce n'est pas déjà fait
4. Retournez sur la page Sécurité
5. Cliquez sur "Mots de passe des applications"
6. Sélectionnez "Autre (nom personnalisé)" et entrez "Shine Banque Website"
7. Cliquez sur "Générer"
8. Copiez le mot de passe de 16 caractères généré

### 3. Remplir le fichier .env

Ouvrez le fichier `.env` et remplissez avec vos informations :

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=shinebanque0@gmail.com
SMTP_PASSWORD=votre_mot_de_passe_application_16_caracteres
SMTP_FROM_NAME=Shine Banque
SMTP_FROM_EMAIL=shinebanque@craft-style.com
```

### 4. Redémarrer le serveur

Après avoir configuré le fichier `.env`, redémarrez le serveur :

```bash
python server.py
```

## Fonctionnement

Lorsqu'un utilisateur remplit le simulateur et soumet sa demande :

1. Le système collecte les informations (nom, email, téléphone, détails du crédit)
2. Un email de confirmation est envoyé automatiquement à l'adresse fournie
3. L'email est personnalisé selon la langue choisie par l'utilisateur (9 langues supportées)
4. L'utilisateur reçoit une confirmation que sa demande sera traitée sous 3 jours ouvrés

## Format de l'email

L'email envoyé est au format HTML professionnel avec :
- En-tête Shine Banque (bleu)
- Message de confirmation personnalisé
- Délai de réponse (3 jours ouvrés)
- Note de non-réponse automatique

## Langues supportées

- 🇫🇷 Français
- 🇬🇧 English
- 🇪🇸 Español
- 🇩🇪 Deutsch
- 🇮🇹 Italiano
- 🇪🇪 Eesti
- 🇱🇹 Lietuvių
- 🇸🇰 Slovenčina
- 🇳🇱 Nederlands

## Dépannage

### Erreur "SMTP credentials not configured"
- Vérifiez que le fichier `.env` existe et contient les bonnes informations
- Redémarrez le serveur après modification du `.env`

### Erreur "Authentication failed"
- Vérifiez que le mot de passe d'application est correct
- Assurez-vous que la validation en 2 étapes est activée sur Gmail
- Vérifiez que l'adresse email est correcte

### L'email n'arrive pas
- Vérifiez le dossier spam/courrier indésirable
- Vérifiez que l'adresse email du destinataire est valide
- Consultez les logs du serveur pour plus de détails
