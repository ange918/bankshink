#!/usr/bin/env python3
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
import subprocess
from email_service import send_confirmation_email

app = Flask(__name__)
CORS(app)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            directory = os.path.dirname(path) or '.'
            filename = os.path.basename(path)
            return send_from_directory(directory, filename)
        elif os.path.isdir(path) and os.path.exists(os.path.join(path, 'index.html')):
            return send_from_directory(path, 'index.html')
    return send_from_directory('.', path)

@app.route('/process_form.php', methods=['POST', 'OPTIONS'])
def process_form_php():
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    
    try:
        import tempfile
        import shutil
        
        # Créer un répertoire temporaire pour les fichiers
        temp_dir = tempfile.mkdtemp()
        
        # Sauvegarder les fichiers uploadés
        files_data = {}
        for field_name in request.files:
            file = request.files[field_name]
            if file and file.filename:
                # Créer un nom de fichier sécurisé
                filename = file.filename
                filepath = os.path.join(temp_dir, filename)
                file.save(filepath)
                
                files_data[field_name] = {
                    'tmp_name': filepath,
                    'name': filename,
                    'type': file.content_type or 'application/octet-stream',
                    'size': os.path.getsize(filepath),
                    'error': 0
                }
        
        # Préparer les données POST
        post_data = dict(request.form)
        
        # Créer un script PHP qui configure $_POST et $_FILES puis inclut process_form.php
        php_wrapper = os.path.join(temp_dir, 'wrapper.php')
        with open(php_wrapper, 'w') as f:
            f.write(f"""<?php
$_POST = json_decode('{json.dumps(post_data)}', true);
$_FILES = json_decode('{json.dumps(files_data)}', true);
$_SERVER['REQUEST_METHOD'] = 'POST';

chdir('{os.getcwd()}');
require 'process_form.php';
?>""")
        
        # Exécuter le script PHP
        result = subprocess.run(
            ['php', php_wrapper],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Nettoyer le répertoire temporaire
        shutil.rmtree(temp_dir, ignore_errors=True)
        
        # Retourner la réponse du PHP
        if result.returncode == 0:
            output = result.stdout.strip()
            # Essayer de parser en JSON
            try:
                response_data = json.loads(output)
                return jsonify(response_data), 200
            except:
                # Si ce n'est pas du JSON, retourner tel quel
                return output, 200, {'Content-Type': 'application/json'}
        else:
            return jsonify({
                'success': False,
                'message': f'Erreur PHP: {result.stderr or result.stdout}'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erreur serveur: {str(e)}'
        }), 500

@app.route('/api/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        
        if not data or 'email' not in data:
            return jsonify({
                'success': False,
                'message': 'Email address is required'
            }), 400
        
        email = data.get('email')
        language = data.get('language', 'fr')
        user_data = data.get('userData', {})
        
        success, message = send_confirmation_email(email, user_data, language)
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Email sent successfully'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': f'Failed to send email: {message}'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Server error: {str(e)}'
        }), 500

if __name__ == '__main__':
    PORT = int(os.getenv('PORT', 5000))
    print(f"🚀 Shine BK website running at http://0.0.0.0:{PORT}")
    print(f"📁 Serving files from: {os.path.abspath('.')}")
    print(f"📧 Email service configured")
    app.run(host='0.0.0.0', port=PORT, debug=False)
