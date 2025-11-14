#!/usr/bin/env python3
"""
Generate complete Dutch versions of all credit pages
Uses the credit-professionnel.html structure as a template
"""

# Define all credit types with their specific content
CREDIT_TYPES = {
    "credit-consommation": {
        "title": "Consumptief krediet",
        "hero_desc": "Realiseer al uw persoonlijke projecten met flexibele en snelle financiering",
        "what_is": "Het consumptief krediet is een persoonlijke lening om uw dagelijkse aankopen te financieren: huishoudelijke apparaten, meubels, reizen, werkzaamheden, enz. Een eenvoudige en snelle oplossing.",
        "rate": "3.5% JKP",
        "delay": "48u",
        "delay_desc": "Geld beschikbaar binnen 48u",
        "amount": "500 tot 100.000 €",
        "tier1_amount": "500 € - 33 000 €",
        "tier2_amount": "33 001 € - 66 000 €",
        "tier3_amount": "66 001 € - 100 000 €",
        "image": "shopping_consumer_cr_6b96e24c.jpg",
        "uses": [
            "Aankoop van huishoudapparaten",
            "Meubels en decoratie",
            "Reizen en vakanties",
            "Werkzaamheden en renovaties"
        ],
        "docs": [
            ("bx-id-card", "Identiteitsbewijs", "Geldig identiteitsbewijs"),
            ("bx-file", "Inkomensbewijzen", "Laatste loonstroken"),
            ("bx-home", "Woonst bewijs", "Elektriciteits- of huurrekening")
        ],
        "cta_title": "Klaar om uw projecten te realiseren?",
        "cta_desc": "Simuleer uw consumptief krediet in enkele klikken"
    },
    "credit-express": {
        "title": "Express krediet",
        "hero_desc": "Dringend geld nodig? Krijg een antwoord binnen 24u en geld binnen 48u",
        "what_is": "Het express krediet is een ultrasnelle financieringsoplossing om aan uw dringende behoeften te voldoen. 100% digitaal proces met antwoord binnen 24u en betaling van de fondsen binnen 48u.",
        "rate": "3.5% JKP",
        "delay": "48u",
        "delay_desc": "Geld beschikbaar binnen 48u",
        "amount": "12.000 tot 500.000 €",
        "tier1_amount": "12 000 € - 175 000 €",
        "tier2_amount": "175 001 € - 350 000 €",
        "tier3_amount": "350 001 € - 500 000 €",
        "image": "fast_speed_express_d_f0605584.jpg",
        "uses": [
            "Dringende medische uitgaven",
            "Spoedherstellingen",
            "Onverwachte opportuniteiten",
            "Dringende zakelijke behoeften"
        ],
        "docs": [
            ("bx-id-card", "Identiteitsbewijs", "Geldig identiteitsbewijs"),
            ("bx-file", "Inkomensbewijzen", "Laatste loonstroken"),
            ("bx-home", "Woonst bewijs", "Elektriciteits- of huurrekening")
        ],
        "cta_title": "Klaar om snel te financieren?",
        "cta_desc": "Simuleer uw express krediet in enkele klikken"
    },
    "credit-immobilier": {
        "title": "Hypotheek",
        "hero_desc": "Word huiseigenaar met de beste vastgoedfinancieringsvoorwaarden",
        "what_is": "De hypotheek stelt u in staat om de aankoop van een onroerend goed te financieren (hoofdverblijf, tweede verblijf of verhuurinvestering). Aantrekkelijke tarieven en persoonlijke begeleiding.",
        "rate": "3.5% JKP",
        "delay": "48u",
        "delay_desc": "Geld beschikbaar binnen 48u",
        "amount": "13.000 tot 100.000 €",
        "tier1_amount": "13 000 € - 40 000 €",
        "tier2_amount": "40 001 € - 70 000 €",
        "tier3_amount": "70 001 € - 100 000 €",
        "image": "modern_house_real_es_cdcc3d77.jpg",
        "uses": [
            "Aankoop van hoofdverblijf",
            "Tweede verblijf",
            "Verhuurinvestering",
            "Werkzaamheden en renovaties"
        ],
        "docs": [
            ("bx-id-card", "Identiteitsbewijs", "Geldig identiteitsbewijs"),
            ("bx-file", "Inkomensbewijzen", "Laatste loonstroken"),
            ("bx-home", "Compromis", "Verkoopovereenkomst")
        ],
        "cta_title": "Klaar om huiseigenaar te worden?",
        "cta_desc": "Simuleer uw hypotheek in enkele klikken"
    },
    "credit-agricole": {
        "title": "Agrarisch krediet",
        "hero_desc": "Financier uw investeringen en landbouwprojecten met voorwaarden aangepast aan de sector",
        "what_is": "Het agrarisch krediet is een gespecialiseerde financiering voor landbouwers, waarmee u kunt investeren in materiaal, land of de exploitatiekasstroom kunt financieren.",
        "rate": "3.5% JKP",
        "delay": "48u",
        "delay_desc": "Geld beschikbaar binnen 48u",
        "amount": "3.000 tot 900.000 €",
        "tier1_amount": "3 000 € - 300 000 €",
        "tier2_amount": "300 001 € - 600 000 €",
        "tier3_amount": "600 001 € - 900 000 €",
        "image": "agriculture_farm_tra_b82ffb56.jpg",
        "uses": [
            "Aankoop van landbouwmachines",
            "Aankoop van land",
            "Financiering van de exploitatie",
            "Modernisering van gebouwen"
        ],
        "docs": [
            ("bx-id-card", "Identiteitsbewijs", "Geldig identiteitsbewijs"),
            ("bx-file", "Boekhoudkundige documenten", "Laatste balansen"),
            ("bx-briefcase", "Bedrijfsdocumenten", "Kbis en statuten")
        ],
        "cta_title": "Klaar om uw exploitatie te ontwikkelen?",
        "cta_desc": "Simuleer uw agrarisch krediet in enkele klikken"
    },
    "credit-digital": {
        "title": "Digitaal krediet",
        "hero_desc": "100% online, 100% snel. Krijg uw krediet zonder verplaatsing, in enkele klikken",
        "what_is": "Het digitaal krediet is een 100% online oplossing om snel een lening te krijgen zonder afspraak of papierwerk. Alles wordt gedaan vanaf uw smartphone of computer.",
        "rate": "3.5% JKP",
        "delay": "48u",
        "delay_desc": "Geld beschikbaar binnen 48u",
        "amount": "500.000 tot 3.000.000 €",
        "tier1_amount": "500 000 € - 1 170 000 €",
        "tier2_amount": "1 170 001 € - 2 070 000 €",
        "tier3_amount": "2 070 001 € - 3 000 000 €",
        "image": "smartphone_digital_t_5effe98f.jpg",
        "uses": [
            "100% online proces",
            "Geen afspraak nodig",
            "Directe validatie",
            "Snelle betaling"
        ],
        "docs": [
            ("bx-id-card", "Digitaal identiteitsbewijs", "Upload uw identiteitsbewijs"),
            ("bx-file", "Elektronische documenten", "PDF van uw bewijsstukken"),
            ("bx-mobile", "Mobiele handtekening", "Onderteken vanaf uw telefoon")
        ],
        "cta_title": "Klaar om 100% online te financieren?",
        "cta_desc": "Simuleer uw digitaal krediet in enkele klikken"
    },
    "credit-automobile": {
        "title": "Autolening",
        "hero_desc": "Financier de aankoop van uw nieuwe of tweedehands voertuig met voordelige voorwaarden",
        "what_is": "De autolening is een lening toegewezen aan de aankoop van een nieuw of gebruikt voertuig. Concurrerende tarieven en financiering tot 100% van de prijs van het voertuig.",
        "rate": "3.5% JKP",
        "delay": "48u",
        "delay_desc": "Geld beschikbaar binnen 48u",
        "amount": "5.000 tot 120.000 €",
        "tier1_amount": "5 000 € - 45 000 €",
        "tier2_amount": "45 001 € - 85 000 €",
        "tier3_amount": "85 001 € - 120 000 €",
        "image": "car_automobile_vehic_f65d7a38.jpg",
        "uses": [
            "Aankoop van nieuwe auto",
            "Aankoop van gebruikte auto",
            "Aankoop van motor",
            "Aankoop van camper"
        ],
        "docs": [
            ("bx-id-card", "Identiteitsbewijs", "Geldig identiteitsbewijs"),
            ("bx-file", "Inkomensbewijzen", "Laatste loonstroken"),
            ("bx-car", "Factuur proforma", "Offerte van de dealer")
        ],
        "cta_title": "Klaar om uw voertuig te kopen?",
        "cta_desc": "Simuleer uw autolening in enkele klikken"
    },
    "micro-credit": {
        "title": "Persoonlijke microkrediet",
        "hero_desc": "Toegang tot kleine leningen voor uw dagelijkse projecten, zonder complicaties",
        "what_is": "Het persoonlijke microkrediet is ontworpen voor kleine financieringsbehoeften. Ideaal voor uw dagelijkse projecten, met een vereenvoudigd aanvraagproces.",
        "rate": "3.5% JKP",
        "delay": "48u",
        "delay_desc": "Geld beschikbaar binnen 48u",
        "amount": "50 tot 8.000 €",
        "tier1_amount": "50 € - 2 600 €",
        "tier2_amount": "2 601 € - 5 300 €",
        "tier3_amount": "5 301 € - 8 000 €",
        "image": "shopping_consumer_cr_6b96e24c.jpg",
        "uses": [
            "Kleine huishoudelijke apparaten",
            "Dringende reparaties",
            "Dagelijkse uitgaven",
            "Kleine projecten"
        ],
        "docs": [
            ("bx-id-card", "Identiteitsbewijs", "Geldig identiteitsbewijs"),
            ("bx-file", "Inkomensbewijzen", "Laatste loonstroken"),
            ("bx-home", "Woonst bewijs", "Elektriciteits- of huurrekening")
        ],
        "cta_title": "Klaar om uw kleine projecten te financieren?",
        "cta_desc": "Simuleer uw microkrediet in enkele klikken"
    },
    "credit-etudiant": {
        "title": "Studentenlening",
        "hero_desc": "Financier uw studies met een lening aangepast aan de behoeften van studenten",
        "what_is": "De studentenlening is speciaal ontworpen om de kosten van hoger onderwijs te dekken: collegegeld, huisvesting, studiemateriaal, levensonderhoud.",
        "rate": "3.5% JKP",
        "delay": "48u",
        "delay_desc": "Geld beschikbaar binnen 48u",
        "amount": "1.000 tot 60.000 €",
        "tier1_amount": "1 000 € - 20 000 €",
        "tier2_amount": "20 001 € - 40 000 €",
        "tier3_amount": "40 001 € - 60 000 €",
        "image": "student_studying_uni_f06360d8.jpg",
        "uses": [
            "Collegegeld",
            "Studentenhuisvesting",
            "Studiemateriaal",
            "Levensonderhoud tijdens studie"
        ],
        "docs": [
            ("bx-id-card", "Identiteitsbewijs", "Geldig identiteitsbewijs"),
            ("bx-file", "Inschrijvingsbewijs", "Certificaat van de instelling"),
            ("bx-user", "Borgsteller", "Document van de borgsteller")
        ],
        "cta_title": "Klaar om uw studies te financieren?",
        "cta_desc": "Simuleer uw studentenlening in enkele klikken"
    }
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Shine BK</title>
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header>
        <div class="header-top">
            <div class="container">
                <div class="contact-info">
                    <span><i class='bx bx-phone'></i> +33 7 45 35 86 52</span>
                    <span><i class='bx bx-envelope'></i> contact@shinebk.com</span>
                </div>
            </div>
        </div>
        <div class="header-main">
            <div class="container">
                <a href="../index.html" class="logo">shine</a>
                <nav>
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="a-propos.html">Over ons</a></li>
                        <li class="dropdown">
                            <a href="nos-offres.html">Onze aanbiedingen ▾</a>
                            <div class="dropdown-menu">
                                <a href="micro-credit.html">Persoonlijke microkrediet</a>
                                <a href="credit-etudiant.html">Studentenlening</a>
                                <a href="credit-professionnel.html">Zakelijke lening</a>
                                <a href="credit-consommation.html">Consumptief krediet</a>
                                <a href="credit-express.html">Express krediet</a>
                                <a href="credit-immobilier.html">Hypotheek</a>
                                <a href="credit-agricole.html">Agrarisch krediet</a>
                                <a href="credit-digital.html">Digitaal krediet</a>
                                <a href="credit-automobile.html">Autolening</a>
                            </div>
                        </li>
                        <li><a href="contact.html">Contact</a></li>
                        <li><a href="simulateur.html" class="btn-primary">Simulator</a></li>
                    </ul>
                </nav>
                <button class="mobile-menu-toggle"><i class='bx bx-menu'></i></button>
            </div>
        </div>
    </header>

    <section class="hero" style="padding: 80px 0;">
        <div class="container">
            <div class="hero-content">
                <h1>{title}</h1>
                <p>{hero_desc}</p>
                <div class="hero-buttons">
                    <a href="simulateur.html" class="btn-primary">Nu simuleren</a>
                    <a href="contact.html" class="btn-secondary">Aanvraag doen</a>
                </div>
            </div>
            <div class="hero-image">
                <img src="../images/{image}" alt="{title}">
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <h2 class="section-title">Wat is een {title_lower}?</h2>
            <p style="max-width: 800px; margin: 0 auto 40px; text-align: center; color: var(--text-light); line-height: 1.8;">
                {what_is}
            </p>
            
            <div class="credit-info-cards">
                <div class="credit-info-card">
                    <div class="credit-info-icon"><i class='bx bx-percentage'></i></div>
                    <h3>Tarief</h3>
                    <p class="credit-info-value">{rate}</p>
                    <p>Jaarlijks kostenpercentage</p>
                </div>
                <div class="credit-info-card">
                    <div class="credit-info-icon"><i class='bx bx-time-five'></i></div>
                    <h3>Termijn</h3>
                    <p class="credit-info-value">{delay}</p>
                    <p>{delay_desc}</p>
                </div>
                <div class="credit-info-card">
                    <div class="credit-info-icon"><i class='bx bx-euro'></i></div>
                    <h3>Bedrag</h3>
                    <p class="credit-info-value">{amount}</p>
                    <p>Beschikbaar bedrag</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section" style="background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);">
        <div class="container">
            <h2 class="section-title" style="margin-bottom: 15px;">Onze serviceniveaus</h2>
            <p style="text-align: center; color: var(--text-light); margin-bottom: 50px; max-width: 700px; margin-left: auto; margin-right: auto;">
                Kies het niveau dat het beste past bij uw financieringsbehoeften
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin-top: 40px;">
                <div style="background: white; padding: 40px 30px; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); text-align: center; border-top: 5px solid #3498db; position: relative; transition: transform 0.3s ease;">
                    <div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: #3498db; color: white; padding: 5px 20px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;">NIVEAU 1</div>
                    <div style="font-size: 3rem; margin: 20px 0; color: #3498db;"><i class='bx bx-user'></i></div>
                    <h3 style="color: var(--primary-blue); margin-bottom: 15px; font-size: 1.8rem;">Standaard</h3>
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 15px; margin: 25px 0;">
                        <div style="font-size: 2.2rem; font-weight: 700; margin-bottom: 5px;">{tier1_amount}</div>
                        <div style="font-size: 0.9rem; opacity: 0.9;">Beschikbaar bedrag</div>
                    </div>
                    <ul style="list-style: none; padding: 0; margin: 25px 0; text-align: left;">
                        <li style="padding: 12px 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> Antwoord binnen 48u</li>
                        <li style="padding: 12px 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> Tarief vanaf 2,5%</li>
                        <li style="padding: 12px 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> 100% online</li>
                        <li style="padding: 12px 0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> Ondersteuning per e-mail</li>
                    </ul>
                    <a href="simulateur.html" class="btn-primary" style="width: 100%; text-align: center; display: inline-block; margin-top: 20px;">Kies Standaard</a>
                </div>

                <div style="background: white; padding: 40px 30px; border-radius: 20px; box-shadow: 0 15px 50px rgba(0,0,0,0.15); text-align: center; border-top: 5px solid var(--gold); position: relative; transform: scale(1.05); z-index: 2;">
                    <div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: var(--gold); color: white; padding: 5px 20px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;">NIVEAU 2 - POPULAIR</div>
                    <div style="font-size: 3rem; margin: 20px 0; color: var(--gold);"><i class='bx bx-crown'></i></div>
                    <h3 style="color: var(--primary-blue); margin-bottom: 15px; font-size: 1.8rem;">Premium</h3>
                    <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 20px; border-radius: 15px; margin: 25px 0;">
                        <div style="font-size: 2.2rem; font-weight: 700; margin-bottom: 5px;">{tier2_amount}</div>
                        <div style="font-size: 0.9rem; opacity: 0.9;">Beschikbaar bedrag</div>
                    </div>
                    <ul style="list-style: none; padding: 0; margin: 25px 0; text-align: left;">
                        <li style="padding: 12px 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> Antwoord binnen 24u</li>
                        <li style="padding: 12px 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> Preferentiële tarieven</li>
                        <li style="padding: 12px 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> Toegewezen adviseur</li>
                        <li style="padding: 12px 0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> Telefonische ondersteuning</li>
                    </ul>
                    <a href="simulateur.html" class="btn-gold" style="width: 100%; text-align: center; display: inline-block; margin-top: 20px; box-shadow: 0 5px 15px rgba(245, 183, 0, 0.3);">Kies Premium</a>
                </div>

                <div style="background: white; padding: 40px 30px; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); text-align: center; border-top: 5px solid #8e44ad; position: relative; transition: transform 0.3s ease;">
                    <div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: #8e44ad; color: white; padding: 5px 20px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;">NIVEAU 3</div>
                    <div style="font-size: 3rem; margin: 20px 0; color: #8e44ad;"><i class='bx bx-trophy'></i></div>
                    <h3 style="color: var(--primary-blue); margin-bottom: 15px; font-size: 1.8rem;">VIP</h3>
                    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); color: #333; padding: 20px; border-radius: 15px; margin: 25px 0;">
                        <div style="font-size: 2.2rem; font-weight: 700; margin-bottom: 5px;">{tier3_amount}</div>
                        <div style="font-size: 0.9rem; opacity: 0.8;">Beschikbaar bedrag</div>
                    </div>
                    <ul style="list-style: none; padding: 0; margin: 25px 0; text-align: left;">
                        <li style="padding: 12px 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> Onmiddellijk antwoord</li>
                        <li style="padding: 12px 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> Beste markttarieven</li>
                        <li style="padding: 12px 0; border-bottom: 1px solid #f0f0f0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> Persoonlijke beheerder</li>
                        <li style="padding: 12px 0; color: var(--text-light);"><i class='bx bx-check' style="color: #27ae60; margin-right: 10px; font-size: 1.3rem;"></i> Prioritaire ondersteuning 24/7</li>
                    </ul>
                    <a href="simulateur.html" class="btn-primary" style="width: 100%; text-align: center; display: inline-block; margin-top: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border: none;">Kies VIP</a>
                </div>
            </div>
        </div>
    </section>

    <section class="section" style="background: var(--light-gray);">
        <div class="container">
            <h2 class="section-title">Mogelijke toepassingen</h2>
            <div style="max-width: 700px; margin: 40px auto;">
                <ul style="list-style: none; padding: 0;">
{uses_list}
                </ul>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="container">
            <h2 class="section-title">Vereiste documenten</h2>
            <div style="max-width: 800px; margin: 40px auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
{docs_list}
            </div>
        </div>
    </section>

    <section class="section" style="background: var(--primary-blue); color: white; text-align: center;">
        <div class="container">
            <h2 style="color: white; margin-bottom: 20px;">{cta_title}</h2>
            <p style="margin-bottom: 30px; font-size: 1.1rem;">{cta_desc}</p>
            <a href="simulateur.html" class="btn-gold">Nu simuleren</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>Shine Bank</h3>
                    <p>Uw digitale bankpartner voor modern en veilig financieel beheer.</p>
                    <div class="social-links">
                        <a href="#"><i class='bx bxl-facebook'></i></a>
                        <a href="#"><i class='bx bxl-twitter'></i></a>
                        <a href="#"><i class='bx bxl-instagram'></i></a>
                        <a href="#"><i class='bx bxl-linkedin'></i></a>
                    </div>
                </div>
                <div class="footer-section">
                    <h3>Snelle links</h3>
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="a-propos.html">Over ons</a></li>
                        <li><a href="nos-offres.html">Onze aanbiedingen</a></li>
                        <li><a href="simulateur.html">Simulator</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Onze kredietaanbiedingen</h3>
                    <ul>
                        <li><a href="micro-credit.html">Persoonlijke microkrediet</a></li>
                        <li><a href="credit-etudiant.html">Studentenlening</a></li>
                        <li><a href="credit-professionnel.html">Zakelijke lening</a></li>
                        <li><a href="credit-consommation.html">Consumptief krediet</a></li>
                        <li><a href="credit-express.html">Express krediet</a></li>
                        <li><a href="credit-immobilier.html">Hypotheek</a></li>
                        <li><a href="credit-agricole.html">Agrarisch krediet</a></li>
                        <li><a href="credit-digital.html">Digitaal krediet</a></li>
                        <li><a href="credit-automobile.html">Autolening</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Contact</h3>
                    <ul>
                        <li><i class='bx bx-map'></i> 123 Avenue des Champs-Élysées, Paris</li>
                        <li><i class='bx bx-phone'></i> +33 7 45 35 86 52</li>
                        <li><i class='bx bx-envelope'></i> contact@shinebk.com</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Shine Bank. Alle rechten voorbehouden. | <a href="#" style="color: rgba(255,255,255,0.6);">Wettelijke kennisgeving</a> | <a href="#" style="color: rgba(255,255,255,0.6);">Privacybeleid</a></p>
            </div>
        </div>
    </footer>

    <script src="../js/main.js"></script>
</body>
</html>
"""

import os

def generate_page(filename, data):
    """Generate a complete Dutch credit page."""
    uses_list = "\n".join([
        f'                    <li style="padding: 15px; background: white; margin-bottom: 10px; border-radius: 8px; border-left: 4px solid var(--gold);"><i class=\'bx bx-check\'></i> {use}</li>'
        for use in data['uses']
    ])
    
    docs_list = "\n".join([
        f'''                <div style="text-align: center; padding: 20px;">
                    <div style="font-size: 3rem; margin-bottom: 10px; color: var(--primary-blue);"><i class="bx {icon}"></i></div>
                    <h4>{title}</h4>
                    <p style="color: var(--text-light); font-size: 0.9rem;">{desc}</p>
                </div>'''
        for icon, title, desc in data['docs']
    ])
    
    html = HTML_TEMPLATE.format(
        title=data['title'],
        title_lower=data['title'].lower(),
        hero_desc=data['hero_desc'],
        what_is=data['what_is'],
        rate=data['rate'],
        delay=data['delay'],
        delay_desc=data['delay_desc'],
        amount=data['amount'],
        tier1_amount=data['tier1_amount'],
        tier2_amount=data['tier2_amount'],
        tier3_amount=data['tier3_amount'],
        image=data['image'],
        uses_list=uses_list,
        docs_list=docs_list,
        cta_title=data['cta_title'],
        cta_desc=data['cta_desc']
    )
    
    for directory in ['pages', 'PACKAGE_HEBERGEUR/pages']:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Generated: {filepath}")

def main():
    print("=" * 60)
    print("Generating Complete Dutch Credit Pages")
    print("=" * 60)
    print()
    
    for filename, data in CREDIT_TYPES.items():
        generate_page(filename + '.html', data)
    
    print()
    print("=" * 60)
    print(f"Successfully generated {len(CREDIT_TYPES)} credit pages!")
    print("=" * 60)

if __name__ == "__main__":
    main()
