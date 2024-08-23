from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.upload import upload_file

app = Flask(__name__)
CORS(app)

# Registrando rotas
app.register_blueprint(upload_file, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
