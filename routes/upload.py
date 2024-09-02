from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from services.process import extract_text_from_pdf, extract_text_from_image
from services.chatgpt import correct_text_with_chatgpt

upload_file = Blueprint('upload_file', __name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_file.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Processar arquivo
        if filename.lower().endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        else:
            text = extract_text_from_image(file_path)

        # Instruções de correção (exemplo)
        instructions = "Corrija a gramática e a ortografia do texto."

        # Enviar texto para o ChatGPT e obter correção
        corrected_text = correct_text_with_chatgpt(text, instructions)

        # Log de depuração
        print(f"Texto original: {text}")
        print(f"Texto corrigido: {corrected_text}")

        return jsonify({"message": "File uploaded and processed successfully", "original_text": text, "corrected_text": corrected_text}), 200
    else:
        return jsonify({"error": "File type not allowed"}), 400
