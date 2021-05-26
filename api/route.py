class Category:
    NEWS = "news"
    WORDS = "words"
    CATEGORIES = "categories"
    OVERALL = "overall"

class Route:
    BASE_API = "/api"
    GET_CATEGORIES = "{0}/{1}".format(BASE_API, Category.CATEGORIES)
    GET_NEWS = "{0}/{1}".format(BASE_API, Category.NEWS)
    GET_WORDS = "{0}/{1}".format(BASE_API, Category.WORDS)
    GET_OVERALL = "{0}/{1}".format(BASE_API, Category.OVERALL)
