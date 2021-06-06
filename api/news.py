from flask import Blueprint, request
from database import Database
from api.route import Category, Route
from model.response import Response

api_news = Blueprint(Category.NEWS, __name__)

@api_news.route(Route.GET_NEWS, methods=["GET"])
def get_news():
    category = request.args.get('id_category')
    time_span = request.args.get('time')

    if not category or not time_span:
        response = Response(data={}, message="Error", status="Bad Request")
        return response.get_json(), 400

    start_date = int(time_span)

    try:
        query = "SELECT * FROM portals WHERE id_category=%s AND date >= CURDATE() - INTERVAL %s DAY"
        db_conn = Database()
        db_response = db_conn.execute(operation=Database.READ, query=query, param=[category, start_date])
        
        multiple_news = []
        for item in db_response.data:
            tags_query= "SELECT tag FROM tags WHERE id_portal=%s"
            tags_response = db_conn.execute(operation=Database.READ, query= tags_query, param=[item[0]])
            news = {
                "id": item[0],
                "portal": item[1],
                "date": item[2],
                "link": item[3],
                "title": item[4],
                "image": item[5],
                "content": item[6],
                "sentiment": item[7],
                "category": item[8],
                "tags": tags_response.data
            }

            multiple_news.append(news)

        response = Response(data=multiple_news, message="OK", status="Get news OK")
        return response.get_json()

    finally:
        db_conn.close()