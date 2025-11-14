#!/usr/bin/env python3
"""Apply comprehensive Dutch translations to main pages"""
import re

# Comprehensive French to Dutch translation dictionary
TRANSLATIONS = {
    # Basic navigation
    "Accueil": "Home",
    "À propos": "Over ons",
    "Nos Offres": "Onze aanbiedingen",
    "Contact": "Contact",
    "Simulateur": "Simulator",
    "S'inscrire": "Inschrijven",
    
    # Credit types
    "Micro-crédit personnel": "Persoonlijke microkrediet",
    "Crédit étudiant": "Studentenlening",
    "Crédit professionnel": "Zakelijke lening",
    "Crédit consommation": "Consumptief krediet",
    "Crédit express": "Express krediet",
    "Crédit immobilier": "Hypotheek",
    "Crédit agricole": "Agrarisch krediet",
    "Crédit digital": "Digitaal krediet",
    "Crédit automobile": "Autolening",
    
    # Titles and headings
    "Banque en ligne premium": "Premium online bankieren",
    "SHINE BANQUE": "SHINE BANK",
    "Shine Banque": "Shine Bank",
    "À propos de Shine Banque": "Over Shine Bank",
    "À propos de Shine Bank": "Over Shine Bank",
    "Contact - Shine BK": "Contact - Shine BK",
    "Simulateur de prêt - Shine BK": "Leningsimulator - Shine BK",
    
    # Hero section
    "Votre partenaire bancaire digital pour une gestion financière moderne et sécurisée. Profitez d'une expérience bancaire exceptionnelle.": "Uw digitale bankpartner voor modern en veilig financieel beheer. Geniet van een uitzonderlijke bankervaring.",
    "En savoir plus": "Meer weten",
    "Simuler mon crédit": "Simuleer mijn krediet",
    
    # About section
    "Shine Banque est votre partenaire financier de confiance depuis plus de 15 ans. Notre mission est de rendre les services bancaires accessibles, transparents et adaptés à vos behoeften.": "Shine Bank is al meer dan 15 jaar uw vertrouwde financiële partner. Onze missie is om bankdiensten toegankelijk, transparant en afgestemd op uw behoeften te maken.",
    "Notre vision est de créer un écosystème financier où chaque client bénéficie d'un accompagnement personnalisé et de solutions innovantes pour réaliser ses projets et sécuriser son avenir.": "Onze visie is om een financieel ecosysteem te creëren waarin elke klant profiteert van persoonlijke ondersteuning en innovatieve oplossingen om zijn doelen te bereiken en zijn toekomst veilig te stellen.",
    
    # Partners section
    "Nos partenaires de confiance": "Onze vertrouwde partners",
    
    # Products section
    "Nos produits": "Onze producten",
    "Des solutions adaptées à tous vos besoins bancaires": "Oplossingen afgestemd op al uw bankbehoeften",
    "Gestion de patrimoine": "Vermogensbeheer",
    "Optimisez votre patrimoine": "Optimaliseer uw vermogen",
    "Assurance vie": "Levensverzekering",
    "Protégez votre avenir": "Bescherm uw toekomst",
    "Trading et bourse": "Trading en beurs",
    "Investissez en toute confiance": "Investeer met vertrouwen",
    "Crédit étudiant": "Studentenlening",
    "Financez vos études": "Financier uw studie",
    "Développez votre entreprise": "Groei uw bedrijf",
    "Réalisez vos projets": "Realiseer uw projecten",
    "Devenez propriétaire": "Word huiseigenaar",
    "100% en ligne, rapide": "100% online, snel",
    "Financez votre véhicule": "Financier uw voertuig",
    "Soutenez votre exploitation": "Ondersteun uw bedrijf",
    
    # Commitments
    "Nos engagements": "Onze verplichtingen",
    "Une plateforme innovante pour gérer vos finances en toute simplicité": "Een innovatief platform om uw financiën gemakkelijk te beheren",
    "Sécurité maximale": "Maximale veiligheid",
    "Vos données et transactions sont protégées par les technologies de cryptage les plus avancées": "Uw gegevens en transacties zijn beschermd door de meest geavanceerde encryptietechnologieën",
    "Rapidité et efficacité": "Snelheid en efficiëntie",
    "Des processus simplifiés pour des décisions de crédit en 24h maximum": "Vereenvoudigde processen voor kredietbeslissingen binnen maximaal 24 uur",
    "Transparence totale": "Totale transparantie",
    "Aucun frais caché, des taux clairs et une communication honnête": "Geen verborgen kosten, duidelijke tarieven en eerlijke communicatie",
    "Support Premium 24/7": "24/7 Premium ondersteuning",
    "Notre équipe d'experts à votre écoute à tout moment pour vous accompagner": "Ons team van experts staat altijd voor u klaar om u te helpen",
    "Finance responsable": "Verantwoorde financiën",
    "Des solutions durables et éthiques pour un avenir financier responsable": "Duurzame en ethische oplossingen voor een verantwoorde financiële toekomst",
    "Innovation digitale": "Digitale innovatie",
    "Une application mobile intuitive et des outils de gestion de pointe": "Een intuïtieve mobiele app en geavanceerde beheertools",
    
    # Stats
    "Notre bilan d'activité": "Onze resultaten",
    "Des chiffres qui témoignent de notre excellence": "Cijfers die getuigen van onze excellentie",
    "Prêts accordés": "Verstrekte leningen",
    "% Satisfaction client": "% Klanttevredenheid",
    "Clients actifs": "Actieve klanten",
    "Années d'expérience": "Jaar ervaring",
    
    # Testimonials
    "Témoignages clients": "Klantbeoordelingen",
    "Ce que nos clients disent de nous": "Wat onze klanten over ons zeggen",
    
    # FAQ
    "Questions Fréquentes (FAQ)": "Veelgestelde vragen (FAQ)",
    "Trouvez rapidement des réponses à vos questions": "Vind snel antwoorden op uw vragen",
    
    # Footer
    "Votre partenaire bancaire digital pour une gestion financière moderne et sécurisée.": "Uw digitale bankpartner voor modern en veilig financieel beheer.",
    "Liens rapides": "Snelle links",
    "Nos offres de crédit": "Onze kredietaanbiedingen",
    "© 2025 Shine Banque. Tous droits réservés.": "© 2025 Shine Bank. Alle rechten voorbehouden.",
    "Mentions légales": "Wettelijke kennisgeving",
    "Politique de confidentialité": "Privacybeleid",
    
    # About page specific
    "Votre partenaire financier de confiance depuis 2010": "Uw vertrouwde financiële partner sinds 2010",
    "Notre Histoire": "Onze geschiedenis",
    "Fondée en 2010, Shine Banque est née de la vision de démocratiser l'accès au crédit et aux services bancaires premium. En 15 ans, nous sommes devenus un acteur majeur de la banque digitale en France, servant plus de 50 000 clients avec excellence et innovation.": "Opgericht in 2010, is Shine Bank ontstaan uit de visie om de toegang tot krediet en premium bankdiensten te democratiseren. In 15 jaar tijd zijn we een belangrijke speler geworden in de digitale bank in Frankrijk, die meer dan 50.000 klanten bedient met excellentie en innovatie.",
    "Notre Mission": "Onze missie",
    "Rendre les services bancaires accessibles, transparents et adaptés aux besoins de chacun grâce à l'innovation digitale.": "Bankdiensten toegankelijk, transparant en afgestemd op ieders behoeften maken dankzij digitale innovatie.",
    "Notre Vision": "Onze visie",
    "Être la banque digitale de référence en Europe, reconnue pour son excellence de service et son innovation.": "De referentie digitale bank in Europa zijn, erkend voor haar uitstekende service en innovatie.",
    "Nos Valeurs": "Onze waarden",
    "Transparence, Innovation, Excellence, Confiance et Engagement envers nos clients.": "Transparantie, Innovatie, Excellentie, Vertrouwen en Toewijding aan onze klanten.",
    "Nos Chiffres Clés": "Onze kerncijfers",
    
    # Contact page
    "Contactez-nous": "Neem contact met ons op",
    "Nous sommes à votre écoute": "We luisteren naar u",
    "Nom complet": "Volledige naam",
    "Votre nom": "Uw naam",
    "Email": "E-mail",
    "Votre email": "Uw e-mailadres",
    "Téléphone": "Telefoon",
    "Votre numéro": "Uw telefoonnummer",
    "Type de demande": "Type aanvraag",
    "Sélectionnez": "Selecteer",
    "Demande de crédit": "Kredietaanvraag",
    "Question générale": "Algemene vraag",
    "Support technique": "Technische ondersteuning",
    "Réclamation": "Klacht",
    "Message": "Bericht",
    "Votre message": "Uw bericht",
    "Envoyer": "Verzenden",
    "Nos Coordonnées": "Onze contactgegevens",
    "Adresse": "Adres",
    "Horaires d'ouverture": "Openingstijden",
    "Lundi - Vendredi": "Maandag - Vrijdag",
    "Samedi": "Zaterdag",
    "Dimanche": "Zondag",
    "Fermé": "Gesloten",
    
    # Simulator page
    "Simulateur de prêt": "Leningsimulator",
    "Calculez votre mensualité": "Bereken uw maandelijkse betaling",
    "Type de crédit": "Type krediet",
    "Montant souhaité": "Gewenst bedrag",
    "Durée du prêt": "Looptijd van de lening",
    "mois": "maanden",
    "an": "jaar",
    "ans": "jaar",
    "Taux d'intérêt annuel": "Jaarlijks rentepercentage",
    "Calculer": "Berekenen",
    "Résultats de la simulation": "Resultaten van de simulatie",
    "Mensualité": "Maandelijkse betaling",
    "Coût total du crédit": "Totale kosten van het krediet",
    "Montant total à rembourser": "Totaal terug te betalen bedrag",
    "TAEG": "JKP",
    "Faire une demande": "Aanvraag indienen",
    "Nouvelle simulation": "Nieuwe simulatie"
}

def apply_translations(content, filepath):
    """Apply all translations to content"""
    for french, dutch in TRANSLATIONS.items():
        content = content.replace(french, dutch)
    return content

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

def main():
    import os
    print("Applying Dutch translations to main pages...")
    for filepath in FILES:
        if not os.path.exists(filepath):
            print(f"  ⚠ Skipped: {filepath}")
            continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        translated = apply_translations(content, filepath)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(translated)
        print(f"  ✓ Translated: {filepath}")
    print("Done!")

if __name__ == "__main__":
    main()
