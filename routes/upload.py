from services.process import extract_text_from_pdf, extract_text_from_image

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

        # Enviar texto para o ChatGPT e obter correção aqui

        return jsonify({"message": "File uploaded and processed successfully", "extracted_text": text}), 200
    else:
        return jsonify({"error": "File type not allowed"}), 400
