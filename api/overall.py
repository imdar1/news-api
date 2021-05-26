from flask import Blueprint, request, Response
from database import Database
from api.route import Category, Route
from model.response import Response
from model.sentiment import Sentiment

api_overall = Blueprint(Category.OVERALL, __name__)

@api_overall.route(Route.GET_OVERALL, methods=["GET"])
def get_overall():
    category = int(request.args.get("id_category"))
    time_span = request.args.get("time")

    if not time_span:
        response = Response(data={}, message="Error", status="Bad Request")
        return response.get_json(), 400

    start_date = int(time_span)
    
    query = ""
    if category:
        query += "SELECT SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)) "
        query += "FROM portals "
        query += "WHERE id_category=%s AND date >= NOW() - INTERVAL %s DAY"
        param = [Sentiment.POSITIVE, Sentiment.NEUTRAL, Sentiment.NEGATIVE, category, start_date]
    else:
        query += "SELECT SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)) "
        query += "FROM portals "
        query += "WHERE date >= NOW() - INTERVAL %s DAY"
        param = [Sentiment.POSITIVE, Sentiment.NEUTRAL, Sentiment.NEGATIVE, start_date]

    print(query)
    db_response = Database.execute(
        operation=Database.READ, 
        query=query, 
        param=param
    )

    print(db_response.data)
    data = {
        "positive": int(db_response.data[0][0] or 0),
        "neutral": int(db_response.data[0][1] or 0),
        "negative": int(db_response.data[0][2] or 0)
    }
    
    response = Response(data=data, message="OK", status="Get overall OK")
    return response.get_json()