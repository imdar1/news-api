from flask import Blueprint, request
from database import Database
from api.route import Category, Route
from model.response import Response

api_categories = Blueprint(Category.CATEGORIES, __name__)

@api_categories.route(Route.GET_CATEGORIES, methods=["GET"])
def get_categories():
    query = "SELECT * FROM categories"
    db_response = Database.execute(operation=Database.READ, query=query, param=[])
    categories = []

    for item in db_response.data:
        category = {
            "id": item[0],
            "category": item[1]
        }
        categories.append(category)

    response = Response(data=categories, message="OK", status="Get categories OK")
    return response.get_json()