#!/usr/bin/env python3
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
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
