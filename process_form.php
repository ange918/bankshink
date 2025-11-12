<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'vendor/autoload.php';

function sendResponse($success, $message) {
    echo json_encode([
        'success' => $success,
        'message' => $message
    ]);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    sendResponse(false, 'Méthode non autorisée');
}

$requiredEnvVars = ['SMTP_HOST', 'SMTP_USERNAME', 'SMTP_PASSWORD', 'SMTP_PORT', 'ADMIN_EMAIL'];
foreach ($requiredEnvVars as $var) {
    if (!getenv($var)) {
        sendResponse(false, "Configuration manquante: $var. Veuillez contacter l'administrateur.");
    }
}

$smtpHost = getenv('SMTP_HOST');
$smtpUsername = getenv('SMTP_USERNAME');
$smtpPassword = getenv('SMTP_PASSWORD');
$smtpPort = (int)getenv('SMTP_PORT');
$adminEmail = getenv('ADMIN_EMAIL');
$fromEmail = getenv('SMTP_FROM_EMAIL') ?: $smtpUsername;
$fromName = getenv('SMTP_FROM_NAME') ?: 'Shine Banque';

$requiredFields = [];
$formData = [];

if (isset($_POST['firstName'])) $formData['Prénom'] = $_POST['firstName'];
if (isset($_POST['lastName'])) $formData['Nom'] = $_POST['lastName'];
if (isset($_POST['email'])) $formData['Email'] = $_POST['email'];
if (isset($_POST['phone'])) $formData['Téléphone'] = $_POST['phone'];
if (isset($_POST['birthdate'])) $formData['Date de naissance'] = $_POST['birthdate'];
if (isset($_POST['amount'])) $formData['Montant'] = $_POST['amount'];
if (isset($_POST['duration'])) $formData['Durée'] = $_POST['duration'];
if (isset($_POST['monthlyPayment'])) $formData['Mensualité'] = $_POST['monthlyPayment'];
if (isset($_POST['message'])) $formData['Message'] = $_POST['message'];

if (empty($formData['Email']) || !filter_var($formData['Email'], FILTER_VALIDATE_EMAIL)) {
    sendResponse(false, 'Adresse email invalide');
}

$clientEmail = $formData['Email'];

$uploadedFiles = [];
$uploadDir = 'uploads/';
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0755, true);
}

if (!empty($_FILES)) {
    foreach ($_FILES as $fieldName => $file) {
        if ($file['error'] === UPLOAD_ERR_OK) {
            $fileName = basename($file['name']);
            $filePath = $uploadDir . uniqid() . '_' . $fileName;
            
            if (move_uploaded_file($file['tmp_name'], $filePath)) {
                $uploadedFiles[] = [
                    'path' => $filePath,
                    'name' => $fileName,
                    'field' => $fieldName
                ];
            }
        }
    }
}

try {
    $mail1 = new PHPMailer(true);
    $mail1->isSMTP();
    $mail1->Host = $smtpHost;
    $mail1->SMTPAuth = true;
    $mail1->Username = $smtpUsername;
    $mail1->Password = $smtpPassword;
    $mail1->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;
    $mail1->Port = $smtpPort;
    $mail1->CharSet = 'UTF-8';
    
    $mail1->setFrom($fromEmail, $fromName);
    $mail1->addAddress($adminEmail);
    $mail1->Subject = 'Nouvelle demande depuis le site Shine Banque';
    
    $bodyAdmin = "<h2>Nouvelle demande reçue</h2>";
    $bodyAdmin .= "<table border='1' cellpadding='10' style='border-collapse: collapse;'>";
    foreach ($formData as $key => $value) {
        $bodyAdmin .= "<tr><td><strong>$key</strong></td><td>" . htmlspecialchars($value) . "</td></tr>";
    }
    $bodyAdmin .= "</table>";
    
    if (!empty($uploadedFiles)) {
        $bodyAdmin .= "<h3>Pièces jointes :</h3><ul>";
        foreach ($uploadedFiles as $file) {
            $bodyAdmin .= "<li>" . htmlspecialchars($file['name']) . " (champ: " . htmlspecialchars($file['field']) . ")</li>";
            $mail1->addAttachment($file['path'], $file['name']);
        }
        $bodyAdmin .= "</ul>";
    }
    
    $mail1->isHTML(true);
    $mail1->Body = $bodyAdmin;
    
    if (!$mail1->send()) {
        sendResponse(false, "Erreur lors de l'envoi à l'administrateur: " . $mail1->ErrorInfo);
    }
    
    $mail2 = new PHPMailer(true);
    $mail2->isSMTP();
    $mail2->Host = $smtpHost;
    $mail2->SMTPAuth = true;
    $mail2->Username = $smtpUsername;
    $mail2->Password = $smtpPassword;
    $mail2->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;
    $mail2->Port = $smtpPort;
    $mail2->CharSet = 'UTF-8';
    
    $mail2->setFrom($fromEmail, $fromName);
    $mail2->addAddress($clientEmail);
    $mail2->Subject = 'Confirmation de votre demande - Shine Banque';
    
    $bodyClient = '<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Confirmation de votre demande</title>
<style>
body {
  font-family: "Segoe UI", sans-serif;
  background-color: #f8f9fb;
  color: #333;
  text-align: center;
  padding: 40px;
}
.container {
  background: white;
  border-radius: 10px;
  padding: 30px;
  max-width: 600px;
  margin: auto;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
h1 {
  color: #003366;
  margin-bottom: 20px;
}
p {
  font-size: 16px;
  line-height: 1.6;
}
.footer {
  margin-top: 30px;
  font-size: 13px;
  color: #888;
}
.logo {
  font-size: 22px;
  font-weight: bold;
  color: #007bff;
  margin-bottom: 20px;
}
</style>
</head>
<body>
  <div class="container">
    <div class="logo">✨ Shine Banque ✨</div>
    <h1>Confirmation de votre demande</h1>
    <p>✅ Votre demande a bien été reçue par <strong>Shine Banque</strong>.</p>
    <p>Vous recevrez une réponse dans un délai de <strong>3 jours ouvrables</strong>.</p>
    <p>Merci de votre confiance.</p>
    <div class="footer">© 2025 Shine Banque – Tous droits réservés.</div>
  </div>
</body>
</html>';
    
    $mail2->isHTML(true);
    $mail2->Body = $bodyClient;
    
    if (!$mail2->send()) {
        sendResponse(false, "Erreur lors de l'envoi de la confirmation: " . $mail2->ErrorInfo);
    }
    
    foreach ($uploadedFiles as $file) {
        if (file_exists($file['path'])) {
            unlink($file['path']);
        }
    }
    
    sendResponse(true, 'Votre demande a bien été envoyée. Vous recevrez un mail de confirmation dans quelques instants.');
    
} catch (Exception $e) {
    sendResponse(false, "Erreur lors de l'envoi: " . $e->getMessage());
}
