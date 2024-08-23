from flask import Flask
from flask_cors import CORS
from routes.upload import upload_file
from routes.delete import delete_file

app = Flask(__name__)
CORS(app)

# Registrando rotas
app.register_blueprint(upload_file, url_prefix='/api')
app.register_blueprint(delete_file, url_prefix='/api')


if __name__ == "__main__":
    app.run(debug=True)
