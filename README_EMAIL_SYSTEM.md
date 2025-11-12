# 📧 Système d'Envoi d'Emails - Shine Banque

## Vue d'ensemble

Ce système permet l'envoi automatique d'emails via le formulaire du site Shine Banque en utilisant PHPMailer avec une configuration SMTP sécurisée.

## 🔧 Configuration

### Prérequis installés
- **PHP 8.2** avec Composer
- **PHPMailer 7.0** - Bibliothèque d'envoi d'emails
- **vlucas/phpdotenv** - Gestion des variables d'environnement (optionnel)

### Variables d'environnement (Secrets Replit)

Les informations SMTP sont stockées de manière sécurisée dans les Secrets Replit. Voici les variables requises :

| Variable | Exemple | Description |
|----------|---------|-------------|
| `SMTP_HOST` | mail.example.com | Serveur SMTP de votre hébergeur |
| `SMTP_USERNAME` | noreply@example.com | Identifiant de connexion SMTP |
| `SMTP_PASSWORD` | ********** | Mot de passe SMTP (à ne jamais partager) |
| `SMTP_PORT` | 465 ou 587 | Port SMTP (465=SMTPS, 587=STARTTLS) |
| `SMTP_FROM_EMAIL` | noreply@example.com | Adresse email expéditeur |
| `SMTP_FROM_NAME` | Votre Entreprise | Nom affiché comme expéditeur |
| `ADMIN_EMAIL` | admin@example.com | Email destinataire des notifications admin |

⚠️ **Important** : Récupérez les vraies valeurs depuis votre panneau Replit Secrets. Ne les stockez jamais dans le code ou la documentation publique.

## 🚀 Fonctionnement

### Script principal : `process_form.php`

Le script gère l'envoi de **2 emails distincts** :

#### 1️⃣ Email à l'administrateur
- **Destinataire** : Défini dans la variable `ADMIN_EMAIL`
- **Contenu** : 
  - Toutes les données du formulaire (nom, email, téléphone, etc.)
  - Pièces jointes (si fournies)
  - Format HTML avec tableau récapitulatif

#### 2️⃣ Email de confirmation au client
- **Destinataire** : Email saisi dans le formulaire
- **Contenu** : Email HTML professionnel et élégant
- **Design** : Template moderne avec logo Shine Banque
- **Message** : Confirmation de réception + délai de réponse (3 jours)

### Détection automatique du chiffrement SMTP

Le script détecte automatiquement le type de chiffrement selon le port :
- **Port 465** → SMTPS (SSL implicite)
- **Autres ports** → STARTTLS (TLS explicite)

```php
$smtpSecure = ($smtpPort == 465) ? PHPMailer::ENCRYPTION_SMTPS : PHPMailer::ENCRYPTION_STARTTLS;
```

### Gestion des fichiers uploadés

✅ **Nettoyage automatique garanti** :
- Les fichiers sont stockés temporairement dans `uploads/`
- Suppression automatique après envoi (succès **ou** erreur)
- Utilisation d'un bloc `finally` pour garantir le nettoyage

⚠️ **Limites recommandées** :
- Taille maximale par fichier : Configurable via PHP (php.ini)
- Types MIME acceptés : Images (JPEG, PNG, GIF) et PDF
- Nombre de fichiers : Limité par la configuration du formulaire
- Pour modifier les limites, ajustez `upload_max_filesize` et `post_max_size` dans la configuration PHP

## 🧪 Page de test

**URL** : `/test_form.html`

Cette page permet de tester le système d'envoi d'emails avec un formulaire complet incluant :
- Champs de texte (nom, prénom, email, téléphone)
- Champs numériques (montant, durée)
- Zone de message
- Upload de fichiers (pièces d'identité)

### Test du système

1. Accéder à : `https://[votre-repl].replit.dev/test_form.html`
2. Remplir le formulaire avec des données de test
3. Cliquer sur "Envoyer le formulaire"
4. Vérifier :
   - ✅ Message de succès dans la page
   - ✅ Email reçu sur l'adresse admin configurée
   - ✅ Email de confirmation reçu sur l'adresse saisie

## 📋 Format de réponse JSON

Le script retourne toujours une réponse JSON :

**Succès** :
```json
{
  "success": true,
  "message": "Votre demande a bien été envoyée. Vous recevrez un mail de confirmation dans quelques instants."
}
```

**Erreur** :
```json
{
  "success": false,
  "message": "Description de l'erreur"
}
```

## 🔒 Sécurité

### ✅ Bonnes pratiques implémentées

1. **Pas de credentials en dur** : Toutes les informations sensibles sont dans les Secrets Replit
2. **Validation des emails** : Vérification avec `filter_var()` et `FILTER_VALIDATE_EMAIL`
3. **Protection XSS** : Utilisation de `htmlspecialchars()` dans les emails
4. **Nettoyage automatique** : Suppression des fichiers temporaires garantie
5. **Headers CORS** : Configuration correcte pour les requêtes cross-origin
6. **Gestion des erreurs** : Try-catch-finally avec messages d'erreur clairs

### ⚠️ Rappels de sécurité

- Ne **jamais** commit les secrets dans Git
- Les secrets sont automatiquement exclus via `.gitignore`
- Le dossier `uploads/` est également exclu du versioning

## 📁 Structure des fichiers

```
.
├── process_form.php        # Script principal d'envoi d'emails
├── test_form.html          # Page de test du formulaire
├── composer.json           # Dépendances PHP
├── vendor/                 # Bibliothèques PHP (gitignored)
├── uploads/                # Fichiers temporaires (gitignored)
└── README_EMAIL_SYSTEM.md  # Cette documentation
```

## 🐛 Débogage

### Problèmes courants

**❌ "Configuration manquante"**
- Vérifier que tous les Secrets sont bien configurés dans Replit
- Relancer le workflow après ajout des secrets

**❌ "Erreur SMTP"**
- Vérifier les credentials SMTP
- Tester la connexion au serveur SMTP sur le port configuré
- Vérifier que le port 465 ou 587 est accessible

**❌ "Adresse email invalide"**
- S'assurer que le champ email est correctement rempli
- Vérifier le format de l'email

## 📞 Support

Pour toute question ou problème :
1. Vérifier les logs du workflow `web_server`
2. Tester avec la page `/test_form.html`
3. Vérifier que tous les Secrets sont configurés

---

**Créé le** : 12 novembre 2025  
**Dernière mise à jour** : 12 novembre 2025  
**Version** : 1.0
