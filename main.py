from flask import Flask 
from flask_cors import CORS
from api.categories import api_categories
from api.overall import api_overall
from api.news import api_news

# from waitress import serve

app = Flask(__name__)
CORS(app)
app.register_blueprint(api_categories)
app.register_blueprint(api_overall)
app.register_blueprint(api_news)

if __name__ == "__main__":
    # serve(app, host='0.0.0.0', port=8080)
    app.run(host="0.0.0.0")