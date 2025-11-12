import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

SMTP_HOST = os.getenv('SMTP_HOST', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
SMTP_USERNAME = os.getenv('SMTP_USERNAME', '')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')
SMTP_FROM_NAME = os.getenv('SMTP_FROM_NAME', 'Shine Banque')
SMTP_FROM_EMAIL = os.getenv('SMTP_FROM_EMAIL', 'shinebanque@craft-style.com')

def get_email_template(language='fr'):
    templates = {
        'fr': {
            'subject': 'Votre demande a bien été reçue – Shine Banque',
            'greeting': 'Bonjour,',
            'message_1': 'Nous avons bien reçu votre demande de simulation.',
            'message_2': 'Notre équipe d\'experts l\'examinera avec attention et vous apportera une réponse dans un délai maximum de <strong>3 jours ouvrés</strong>.',
            'message_3': 'Merci pour votre confiance.',
            'message_4': 'L\'équipe <strong>Shine Banque</strong> reste à votre disposition pour tout complément d\'information.',
            'footer': 'Cet e-mail a été envoyé automatiquement. Merci de ne pas y répondre directement.'
        },
        'en': {
            'subject': 'Your request has been received – Shine Bank',
            'greeting': 'Hello,',
            'message_1': 'We have received your simulation request.',
            'message_2': 'Our team of experts will review it carefully and provide you with a response within a maximum of <strong>3 business days</strong>.',
            'message_3': 'Thank you for your trust.',
            'message_4': 'The <strong>Shine Bank</strong> team remains at your disposal for any additional information.',
            'footer': 'This email was sent automatically. Please do not reply directly.'
        },
        'es': {
            'subject': 'Su solicitud ha sido recibida – Shine Banco',
            'greeting': 'Hola,',
            'message_1': 'Hemos recibido su solicitud de simulación.',
            'message_2': 'Nuestro equipo de expertos la examinará cuidadosamente y le proporcionará una respuesta en un plazo máximo de <strong>3 días hábiles</strong>.',
            'message_3': 'Gracias por su confianza.',
            'message_4': 'El equipo de <strong>Shine Banco</strong> permanece a su disposición para cualquier información adicional.',
            'footer': 'Este correo electrónico fue enviado automáticamente. Por favor, no responda directamente.'
        },
        'de': {
            'subject': 'Ihre Anfrage wurde empfangen – Shine Bank',
            'greeting': 'Hallo,',
            'message_1': 'Wir haben Ihre Simulationsanfrage erhalten.',
            'message_2': 'Unser Expertenteam wird sie sorgfältig prüfen und Ihnen innerhalb von maximal <strong>3 Werktagen</strong> eine Antwort geben.',
            'message_3': 'Vielen Dank für Ihr Vertrauen.',
            'message_4': 'Das Team von <strong>Shine Bank</strong> steht Ihnen jederzeit für weitere Informationen zur Verfügung.',
            'footer': 'Diese E-Mail wurde automatisch gesendet. Bitte antworten Sie nicht direkt darauf.'
        },
        'it': {
            'subject': 'La tua richiesta è stata ricevuta – Shine Banca',
            'greeting': 'Ciao,',
            'message_1': 'Abbiamo ricevuto la tua richiesta di simulazione.',
            'message_2': 'Il nostro team di esperti la esaminerà attentamente e ti fornirà una risposta entro un massimo di <strong>3 giorni lavorativi</strong>.',
            'message_3': 'Grazie per la tua fiducia.',
            'message_4': 'Il team di <strong>Shine Banca</strong> rimane a tua disposizione per qualsiasi informazione aggiuntiva.',
            'footer': 'Questa email è stata inviata automaticamente. Si prega di non rispondere direttamente.'
        },
        'et': {
            'subject': 'Teie taotlus on vastu võetud – Shine Pank',
            'greeting': 'Tere,',
            'message_1': 'Oleme saanud teie simulatsioonitaotluse.',
            'message_2': 'Meie ekspertide meeskond vaatab selle hoolikalt läbi ja annab teile vastuse maksimaalselt <strong>3 tööpäeva</strong> jooksul.',
            'message_3': 'Täname teid usalduse eest.',
            'message_4': '<strong>Shine Panga</strong> meeskond on teie teenistuses mis tahes lisateabe saamiseks.',
            'footer': 'See e-kiri saadeti automaatselt. Palun ärge vastake otse.'
        },
        'lt': {
            'subject': 'Jūsų užklausa gauta – Shine Bankas',
            'greeting': 'Sveiki,',
            'message_1': 'Gavome jūsų simuliacijos užklausą.',
            'message_2': 'Mūsų ekspertų komanda ją atidžiai peržiūrės ir pateiks jums atsakymą per maksimaliai <strong>3 darbo dienas</strong>.',
            'message_3': 'Dėkojame už pasitikėjimą.',
            'message_4': '<strong>Shine Banko</strong> komanda lieka jūsų paslaugose dėl bet kokios papildomos informacijos.',
            'footer': 'Šis el. laiškas buvo išsiųstas automatiškai. Prašome neatsakyti tiesiogiai.'
        },
        'sk': {
            'subject': 'Vaša žiadosť bola prijatá – Shine Banka',
            'greeting': 'Dobrý deň,',
            'message_1': 'Prijali sme vašu žiadosť o simuláciu.',
            'message_2': 'Náš tím expertov ju pozorne preskúma a poskytne vám odpoveď do maximálne <strong>3 pracovných dní</strong>.',
            'message_3': 'Ďakujeme za vašu dôveru.',
            'message_4': 'Tím <strong>Shine Banky</strong> zostáva k dispozícii pre akékoľvek dodatočné informácie.',
            'footer': 'Tento e-mail bol odoslaný automaticky. Neodpovedajte priamo na neho.'
        },
        'nl': {
            'subject': 'Uw aanvraag is ontvangen – Shine Bank',
            'greeting': 'Hallo,',
            'message_1': 'We hebben uw simulatieaanvraag ontvangen.',
            'message_2': 'Ons team van experts zal deze zorgvuldig beoordelen en u binnen maximaal <strong>3 werkdagen</strong> een antwoord geven.',
            'message_3': 'Bedankt voor uw vertrouwen.',
            'message_4': 'Het team van <strong>Shine Bank</strong> blijft tot uw beschikking voor eventuele aanvullende informatie.',
            'footer': 'Deze e-mail is automatisch verzonden. Gelieve niet rechtstreeks te antwoorden.'
        }
    }
    return templates.get(language, templates['fr'])

def send_confirmation_email(to_email, user_data, language='fr'):
    if not SMTP_USERNAME or not SMTP_PASSWORD:
        raise Exception("SMTP credentials not configured. Please set up your .env file.")
    
    template = get_email_template(language)
    
    html_content = f"""
    <html>
    <body style="font-family: 'Montserrat', Arial, sans-serif; background-color: #f5f6fa; padding: 20px; margin: 0;">
      <div style="max-width: 600px; margin: auto; background: white; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); overflow: hidden;">
        <div style="background-color: #1a73e8; color: white; padding: 20px 30px; font-size: 24px; font-weight: bold;">
          Shine Banque
        </div>
        <div style="padding: 30px;">
          <h2 style="color: #333; margin-top: 0;">{template['greeting']}</h2>
          <p style="color: #555; font-size: 16px; line-height: 1.6;">
            {template['message_1']}<br>
            {template['message_2']}
          </p>
          <p style="color: #555; font-size: 16px; line-height: 1.6;">
            {template['message_3']}<br>
            {template['message_4']}
          </p>
          <hr style="border:none; border-top:1px solid #ddd; margin:30px 0;">
          <p style="font-size:14px; color:#888; margin: 0;">
            {template['footer']}
          </p>
        </div>
      </div>
    </body>
    </html>
    """
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = template['subject']
    msg['From'] = f"{SMTP_FROM_NAME} <{SMTP_FROM_EMAIL}>"
    msg['To'] = to_email
    
    html_part = MIMEText(html_content, 'html')
    msg.attach(html_part)
    
    try:
        if SMTP_PORT == 465:
            server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=10)
        else:
            server = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10)
            server.starttls()
        
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True, "Email sent successfully"
    except Exception as e:
        return False, str(e)
