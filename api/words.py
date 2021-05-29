from flask import Blueprint, request
from database import Database
from api.route import Category, Route
from model.response import Response

api_words = Blueprint(Category.WORDS, __name__)


@api_words.route(Route.GET_WORDS, methods=["GET"])
def get_words():
    query = "SELECT words_positif.word,\
     SUM(words_positif.value) + SUM(words_negatif.value) as frekuensi \
     FROM words_negatif INNER JOIN words_positif ON words_negatif.value = words_positif.value \
     GROUP BY words_positif.word ORDER BY frekuensi DESC LIMIT 1"
    # query = "SELECT * FROM words_negatif"
    db_response = Database.execute(operation=Database.READ, query=query, param=[])
    print(db_response)
    negative_data = []
    no = 1
    for item in db_response.data:
        print(item)
        new_data = {
            "id": ++no,
            "word": item[0],
            "frequency": int(item[1])
        }
        negative_data.append(new_data)

    response = Response(data=negative_data, message='OK', status="get Ok")
    return response.get_json()