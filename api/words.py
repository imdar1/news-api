from flask import Blueprint, request
from database import Database
from api.route import Category, Route
from model.response import Response

api_words = Blueprint(Category.WORDS, __name__)


@api_words.route(Route.GET_WORDS, methods=["GET"])
def get_words():
    category = request.args.get("id_category")
    time_span = request.args.get("time")
    length = request.args.get("length")

    if not length:
        length = 5

    if not time_span:
        response = Response(data={}, message="Error", status="Bad Request")
        return response.get_json(), 400

    start_date = int(time_span)

    if not category:
        positive_query = "SELECT word, SUM(value) AS freq \
         FROM words_positif \
         WHERE date >= CURDATE() - INTERVAL %s DAY \
         GROUP BY word \
         ORDER BY freq DESC \
         LIMIT %s"
        negative_query = "SELECT word, SUM(value) AS freq \
         FROM words_negatif \
         WHERE date >= CURDATE() - INTERVAL %s DAY \
         GROUP BY word \
         ORDER BY freq DESC \
         LIMIT %s"
        positive_params = [ start_date, length ] 
        negative_params = [ start_date, length ]
    else:
        positive_query = "SELECT word, SUM(value) AS freq \
         FROM words_positif \
         WHERE id_category=%s AND date >= CURDATE() - INTERVAL %s DAY \
         GROUP BY word \
         ORDER BY freq DESC \
         LIMIT %s"
        positive_query = "SELECT word, SUM(value) AS freq \
         FROM words_negatif \
         WHERE id_category=%s AND date >= CURDATE() - INTERVAL %s DAY \
         GROUP BY word \
         ORDER BY freq DESC \
         LIMIT %s"
        positive_params = [ category, start_date, length ]
        negative_params = [ category, start_date, length ]

    db_response = Database.execute(operation=Database.READ, query=positive_query, param=positive_params)
    positive_words = []
    for item in db_response.data:
        positive_data = {
            "word": item[0],
            "frequency": int(item[1])
        }
        positive_words.append(positive_data)

    db_response = Database.execute(operation=Database.READ, query=negative_query, param=negative_params)
    negative_words = []
    for item in db_response.data:
        negative_data = {
            "word": item[0],
            "frequency": int(item[1])
        }
        negative_words.append(negative_data)

    response_data = {
        "positive": positive_words,
        "negative": negative_words
    }
    response = Response(data=response_data, message='OK', status="get words Ok")
    return response.get_json()