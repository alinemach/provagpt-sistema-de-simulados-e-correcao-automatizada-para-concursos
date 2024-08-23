from flask import Blueprint, request, jsonify
import os

delete_file = Blueprint('delete_file', __name__)

UPLOAD_FOLDER = 'uploads'

@delete_file.route('/delete', methods=['DELETE'])
def delete_file():
    filename = request.args.get('filename')
    if not filename:
        return jsonify({"error": "Filename parameter is missing"}), 400
    
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    
    if os.path.isfile(file_path):
        os.remove(file_path)
        return jsonify({"message": f"File {filename} deleted successfully"}), 200
    else:
        return jsonify({"error": "File not found"}), 404
