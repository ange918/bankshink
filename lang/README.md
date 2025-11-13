# Système Multilingue - Shine Banque

Ce dossier contient tous les fichiers de traduction JSON pour le site web Shine Banque.

## 📁 Structure des Fichiers

```
lang/
├── fr.json          # Français (langue par défaut)
├── en.json          # English
├── es.json          # Español
├── de.json          # Deutsch
├── it.json          # Italiano
├── et.json          # Eesti
├── lt.json          # Lietuvių
├── sk.json          # Slovenčina
├── nl.json          # Nederlands
├── pt.json          # Português
├── KEYS_LIST.md     # Liste exhaustive de toutes les clés
└── README.md        # Ce fichier
```

## 🌍 Langues Disponibles

| Code | Langue | Fichier |
|------|--------|---------|
| `fr` | Français | fr.json |
| `en` | English | en.json |
| `es` | Español | es.json |
| `de` | Deutsch | de.json |
| `it` | Italiano | it.json |
| `et` | Eesti | et.json |
| `lt` | Lietuvių | lt.json |
| `sk` | Slovenčina | sk.json |
| `nl` | Nederlands | nl.json |
| `pt` | Português | pt.json |

## 📊 Statistiques

- **Nombre total de langues** : 10
- **Nombre total de clés** : 102 par langue
- **Total de traductions** : 1,020 (102 × 10)

## 🔑 Catégories de Clés

Les clés de traduction sont organisées par section :

### Contact & Communication
- `phone`, `email`

### Navigation (`nav_*`)
- Tous les liens de navigation du menu principal

### Offres de Crédit (`offer_*`)
- Les 9 types de crédits proposés

### Section Hero (`hero_*`)
- Titre principal, sous-titre, description, boutons d'action

### À Propos (`about_*`)
- Informations sur l'entreprise

### Produits (`product_*`)
- 10 produits avec titre et description

### Engagements (`commitment_*`)
- 6 engagements de l'entreprise

### Statistiques (`stats_*`)
- Chiffres clés de l'entreprise

### Témoignages (`testimonials_*`)
- Section des avis clients

### FAQ (`faq_*`)
- Questions fréquentes

### Footer (`footer_*`)
- Pied de page

### Niveaux de Service (`tier_*`)
- 3 niveaux avec caractéristiques

## 💡 Utilisation

### 1. Charger un fichier de traduction

```javascript
// Exemple : Charger les traductions françaises
fetch('lang/fr.json')
  .then(response => response.json())
  .then(translations => {
    console.log(translations.hero_title); // "SHINE BANQUE"
  });
```

### 2. Utiliser avec le système existant

Le fichier `js/translations.js` contient déjà toutes ces traductions intégrées. Les fichiers JSON du dossier `lang/` sont fournis pour :
- Faciliter la maintenance
- Permettre l'importation dans d'autres systèmes
- Servir de référence pour de nouvelles traductions

### 3. Ajouter une nouvelle clé

Pour ajouter une nouvelle clé de traduction :

1. Ajoutez la clé dans TOUS les fichiers JSON (fr.json, en.json, etc.)
2. Utilisez un format cohérent : `section_element_type`
3. Mettez à jour le fichier KEYS_LIST.md
4. Mettez à jour `js/translations.js` si nécessaire

Exemple :
```json
{
  "new_section_title": "Nouveau Titre"
}
```

### 4. Utiliser dans le HTML

```html
<!-- Méthode actuelle avec data-translate -->
<h1 data-translate="hero_title">SHINE BANQUE</h1>

<!-- Le JavaScript translations.js remplacera automatiquement le texte -->
```

## 🔄 Synchronisation

Les fichiers JSON de ce dossier et le fichier `js/translations.js` doivent rester synchronisés.

**Important** : Si vous modifiez :
- Les fichiers JSON → Mettez à jour `js/translations.js`
- Le fichier `js/translations.js` → Mettez à jour les fichiers JSON

## ✅ Validation

Tous les fichiers JSON ont été validés pour :
- ✅ Format JSON correct
- ✅ Même nombre de clés (102) dans chaque fichier
- ✅ Aucune clé manquante
- ✅ Aucune duplication
- ✅ Cohérence des valeurs (phone, email identiques partout)

## 📝 Conventions de Nommage

Format des clés : `section_element_[type]`

Exemples :
- `hero_title` → Titre de la section hero
- `product_1_desc` → Description du produit 1
- `tier_2_feature_3` → 3ème caractéristique du niveau 2

## 🚀 Workflow de Traduction

1. **Extraction** : Identifier tous les textes du site
2. **Création des clés** : Nommer chaque texte avec une clé unique
3. **Traduction** : Traduire dans toutes les langues
4. **Validation** : Vérifier la cohérence
5. **Intégration** : Utiliser dans le code HTML/JavaScript

## 📚 Documentation Complète

Consultez le fichier `KEYS_LIST.md` pour :
- La liste complète des 102 clés
- La description de chaque clé
- L'organisation par catégorie
- Les statistiques détaillées

## 🔧 Maintenance

Pour maintenir ce système :
1. Gardez tous les fichiers synchronisés
2. Testez chaque langue après modification
3. Documentez les nouvelles clés
4. Respectez les conventions de nommage

## 📞 Support

Pour toute question concernant le système multilingue, consultez :
- KEYS_LIST.md - Liste exhaustive des clés
- js/translations.js - Implémentation JavaScript
- Ce fichier - Documentation générale
