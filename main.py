from flask import Flask 
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    # serve(app, host='0.0.0.0', port=8080)
    app.run(host="0.0.0.0")