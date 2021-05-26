from flask import Blueprint, request
from database import Database
from route import Category, Route
from model.response import Response

api_words = Blueprint(Category.WORDS, __name__)

@api_words.route(Route.GET_WORDS, methods=["GET"])
def get_words():
    pass