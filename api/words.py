from flask import Blueprint, request
from database import Database
from route import Category, Route
from model.response import Response

api_news = Blueprint(Category.WORDS, __name__)

@api_news.route(Route.WORDS, method=["GET"])
def get_words():
    pass