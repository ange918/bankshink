# Shine BK - Plateforme Bancaire en ligne

## Vue d'ensemble
Site web complet pour Shine Banque, une plateforme de prêt en ligne premium. Le site est développé en HTML, CSS et JavaScript pur, sans frameworks, avec un design moderne et responsive.

## Couleurs principales
- Bleu principal : #0044cc
- Bleu foncé : #002b7a
- Blanc : #ffffff
- Or : #f5b700

## Typographie
- Titres et textes : Montserrat (Google Fonts)
- Poids utilisés : 300, 400, 500, 600, 700, 800

## Structure du projet
```
/
├── index.html              # Page d'accueil
├── server.py              # Serveur Flask (port 5000) avec API d'emails
├── email_service.py       # Service d'envoi d'emails SMTP multilingue
├── .env.example           # Exemple de configuration SMTP
├── CONFIGURATION_SMTP.md  # Guide de configuration des emails
├── css/
│   └── style.css          # Styles globaux
├── js/
│   ├── main.js            # JavaScript pour animations et interactions
│   └── translations.js    # Système de traduction 9 langues
├── images/                # Images libres de droits
└── pages/
    ├── simulateur.html           # Page simulateur de prêt
    ├── contact.html              # Page de contact
    ├── micro-credit.html         # Micro-crédit personnel
    ├── credit-etudiant.html      # Crédit étudiant
    ├── credit-professionnel.html # Crédit professionnel
    ├── credit-consommation.html  # Crédit consommation
    ├── credit-express.html       # Crédit express
    ├── credit-immobilier.html    # Crédit immobilier
    ├── credit-agricole.html      # Crédit agricole
    ├── credit-digital.html       # Crédit digital
    └── credit-automobile.html    # Crédit automobile
```

## Fonctionnalités principales
1. **Page d'accueil** : Hero section, présentation des produits, engagements, statistiques
2. **Simulateur de prêt** : Calcul dynamique des mensualités avec 9 types de crédits + envoi email
3. **Page Contact** : Formulaire avec validation et informations de contact
4. **Pages produits** : Pages détaillées pour chaque type de crédit
5. **Design responsive** : Compatible PC, tablette, mobile
6. **Animations** : Fade-in au scroll, hover effects, compteurs animés
7. **Multi-langues** : 9 langues complètes (FR/EN/ES/DE/IT/ET/LT/SK/NL)
8. **Emails SMTP** : Confirmation automatique multilingue via Flask
9. **Carrousel partenaires** : 11 logos réels d'institutions financières

## 9 types de crédits proposés
1. Micro-crédit personnel
2. Crédit étudiant
3. Crédit professionnel
4. Crédit consommation
5. Crédit express
6. Crédit immobilier
7. Crédit agricole
8. Crédit digital
9. Crédit automobile

## Lancement du site
Le site est servi par un serveur HTTP Python sur le port 5000.
Le workflow est configuré automatiquement pour démarrer le serveur.

## Notes de développement
- Cache désactivé pour faciliter le développement
- Menu déroulant pour "Nos Offres" avec les 9 types de crédits
- Formulaire de simulation avec calcul des mensualités selon la formule financière standard
- Formulaire de contact avec validation et message de confirmation

## État actuel
✅ Page d'accueil avec hero, produits, engagements, stats
✅ Page simulateur fonctionnelle avec calcul des mensualités
✅ Page contact avec formulaire de validation
✅ 9 pages de produits complètes avec détails pour chaque type de crédit
✅ Design responsive et animations
✅ Navigation avec menu déroulant fonctionnel (9 types de crédits)
✅ Footer avec liens et réseaux sociaux
✅ Toutes les pages interconnectées avec navigation cohérente

## Pages de crédits (9 pages complètes)
- ✅ pages/micro-credit.html - Micro-crédit personnel (500€ à 10 000€)
- ✅ pages/credit-etudiant.html - Crédit étudiant (jusqu'à 50 000€)
- ✅ pages/credit-professionnel.html - Crédit professionnel (10 000€ à 500 000€)
- ✅ pages/credit-consommation.html - Crédit consommation (1 000€ à 75 000€)
- ✅ pages/credit-express.html - Crédit express (500€ à 15 000€, délai 48h)
- ✅ pages/credit-immobilier.html - Crédit immobilier (jusqu'à 100% du projet)
- ✅ pages/credit-agricole.html - Crédit agricole (20 000€ à 1 000 000€)
- ✅ pages/credit-digital.html - Crédit digital 100% en ligne (1 000€ à 50 000€)
- ✅ pages/credit-automobile.html - Crédit automobile (3 000€ à 80 000€)

## Modifications récentes
- 07/11/2025 : **SESSION 2** - Système d'emails SMTP et carrousel partenaires
  - ✅ **Traductions complètes** : Menu dropdown "Nos Offres" traduit dans les 9 langues
  - ✅ **Carrousel partenaires** : Remplacement par 11 logos réels (Nickel, CIC, Slovenská sporiteľňa, Swedbank, mBank, BBVA, Trade Republic, Orange Bank, BRED, UE, Portugal)
  - ✅ **Système d'emails SMTP** : Serveur Flask avec API `/api/send-email`
  - ✅ **Service email multilingue** : Templates d'emails dans les 9 langues (email_service.py)
  - ✅ **Configuration SMTP** : Fichiers .env.example et CONFIGURATION_SMTP.md créés
  - ✅ **Intégration simulateur** : Envoi automatique d'email de confirmation après simulation
  - ✅ **Messages multilingues** : Confirmations et erreurs traduites dans toutes les langues
- 07/11/2025 : **SESSION 1** - Améliorations majeures du design et de la fonctionnalité
  - ✅ Bouton "En savoir plus" : fond blanc avec texte bleu pour meilleure visibilité
  - ✅ Sélecteur de langue : texte bleu sur fond blanc, parfaitement lisible
  - ✅ Ajout de 4 nouvelles langues : Estonien 🇪🇪, Lituanien 🇱🇹, Slovaque 🇸🇰, Néerlandais 🇳🇱
  - ✅ Système de traduction créé (translations.js) avec 9 langues complètes
  - ✅ Image de la section "À propos" remplacée par une famille heureuse
  - ✅ Suppression du bouton "Découvrir nos valeurs"
  - ✅ Remplacement de TOUS les emojis par des Boxicons officiels sur TOUTES les pages
  - ✅ Amélioration du dimensionnement et centrage des images sur tout le site
  - ✅ Sélecteur de langue à 9 options ajouté sur toutes les 13 pages
  - ✅ Script translations.js chargé sur toutes les pages
- 06/11/2025 : Mise à jour du design du site
  - Section hero redesignée : textes centrés avec image en arrière-plan
  - Intégration de Boxicons pour remplacer tous les emojis
  - Formulaire multi-étapes (4 étapes) dans le simulateur de crédit
  - Header uniformisé sur toutes les pages avec navigation cohérente
  - Footer mis à jour avec toutes les 9 offres de crédit
  - Correction du bug JavaScript du slider de témoignages
- 05/11/2025 : Création initiale du site avec structure complète
- 05/11/2025 : Ajout des 8 pages de crédits manquantes pour compléter les 9 types
- Images libres de droits téléchargées depuis Unsplash/Pexels
- Serveur HTTP configuré sur port 5000 avec cache control
- Tous les liens du menu déroulant fonctionnels

## Système de traduction
Un système de traduction complet a été implémenté avec 9 langues :
- Français 🇫🇷, Anglais 🇬🇧, Espagnol 🇪🇸, Allemand 🇩🇪, Italien 🇮🇹
- Estonien 🇪🇪, Lituanien 🇱🇹, Slovaque 🇸🇰, Néerlandais 🇳🇱

Le fichier `js/translations.js` contient toutes les traductions et le système de changement de langue.
Tous les éléments du site sont traduits : navigation, menu dropdown, formulaires, boutons, messages.

## Système d'emails SMTP
Un système d'envoi d'emails a été intégré avec Flask :
- **API endpoint** : `/api/send-email` (POST)
- **Templates multilingues** : 9 langues avec subject, greeting, messages, footer
- **Configuration** : Via fichier `.env` (voir `.env.example` et `CONFIGURATION_SMTP.md`)
- **Intégration** : Envoi automatique après soumission du simulateur
- **Sécurité** : Gestion des erreurs et validation des données

### Configuration requise pour les emails
1. Créer un fichier `.env` depuis `.env.example`
2. Configurer les paramètres SMTP (Gmail recommandé avec mot de passe d'application)
3. Redémarrer le serveur Flask

Consultez `CONFIGURATION_SMTP.md` pour les instructions détaillées.

## Carrousel des partenaires
Le carrousel affiche 11 logos réels d'institutions financières européennes :
- Nickel, CIC, Slovenská sporiteľňa, Swedbank, mBank
- BBVA, Trade Republic, Orange Bank, BRED
- Drapeaux : Union Européenne, Portugal
- Animation défilement automatique fluide
