from app import app, db
import os
from whatsapp_handler import Whatsapp_handler
from flask import request, jsonify, url_for, send_from_directory, send_file, redirect, url_for
from excel_exports import export_msg
import json

@app.route('/chat2desk', methods=['GET', 'POST'])
def chat2desk():
    if request.method == 'POST':
        whatsapp = Whatsapp_handler(request.json)
        whatsapp.add_message()
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    return 'hello'

@app.route('/export_messages', methods=['GET', 'POST'])
def export_messages():
    file = export_msg()
    return redirect('http://188.225.86.179/download_file/{}'.format(file))

@app.route('/download_file/<filename>', methods=['GET', 'POST'])
def download_file(filename):
    file = filename
    return send_from_directory('/home/mantis/msg-parser/excels', file)


