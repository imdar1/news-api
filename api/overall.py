from flask import Blueprint, request, Response
from database import Database
from api.route import Category, Route
from model.response import Response
from model.sentiment import Sentiment

api_overall = Blueprint(Category.OVERALL, __name__)

def get_n_latest_day_sentiment(id_category, day):
    result = []
    try:
        db_conn = Database()
        for i in range(day):
            if id_category > 0:
                query = "SELECT SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)) \
                 FROM portals \
                 WHERE id_category=%s AND date = CURDATE() - INTERVAL %s DAY"
                param = [Sentiment.POSITIVE, Sentiment.NEUTRAL, Sentiment.NEGATIVE, id_category, i]
            else:
                query = "SELECT SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)) \
                FROM portals \
                WHERE date = CURDATE() - INTERVAL %s DAY"
                param = [Sentiment.POSITIVE, Sentiment.NEUTRAL, Sentiment.NEGATIVE, i]
            
            db_response = db_conn.execute(
                operation=Database.READ, 
                query=query, 
                param=param
            )
            data = {
                "positive": int(db_response.data[0][0] or 0),
                "neutral": int(db_response.data[0][1] or 0),
                "negative": int(db_response.data[0][2] or 0)
            }
            result.append(data)
        return result
    finally:
        db_conn.close()

@api_overall.route(Route.GET_OVERALL_CHART, methods=["GET"])
def get_chart_overall():
    category = int(request.args.get("id_category") or 0)
    time_span = request.args.get("time")

    if not time_span:
        response = Response(data={}, message="Error", status="Bad Request")
        return response.get_json(), 400

    start_date = int(time_span)

    response = Response(data=get_n_latest_day_sentiment(category, start_date), message="OK", status="Get chart OK")
    return response.get_json()

@api_overall.route(Route.GET_OVERALL, methods=["GET"])
def get_overall():
    category = request.args.get("id_category")
    time_span = request.args.get("time")

    if not time_span:
        response = Response(data={}, message="Error", status="Bad Request")
        return response.get_json(), 400

    start_date = int(time_span)
    
    try:
        query = ""
        if category:
            query += "SELECT SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)) "
            query += "FROM portals "
            query += "WHERE id_category=%s AND date >= CURDATE() - INTERVAL %s DAY"
            param = [Sentiment.POSITIVE, Sentiment.NEUTRAL, Sentiment.NEGATIVE, category, start_date]
        else:
            query += "SELECT SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)), SUM(IF(sentiment=%s, 1, 0)) "
            query += "FROM portals "
            query += "WHERE date >= CURDATE() - INTERVAL %s DAY"
            param = [Sentiment.POSITIVE, Sentiment.NEUTRAL, Sentiment.NEGATIVE, start_date]

        db_conn = Database()
        db_response = db_conn.execute(
            operation=Database.READ, 
            query=query, 
            param=param
        )

        data = {
            "positive": int(db_response.data[0][0] or 0),
            "neutral": int(db_response.data[0][1] or 0),
            "negative": int(db_response.data[0][2] or 0)
        }
        
        response = Response(data=data, message="OK", status="Get overall OK")
        return response.get_json()
    
    finally:
        db_conn.close()