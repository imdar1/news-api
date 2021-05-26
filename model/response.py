from flask import jsonify

class Response:
    KEY_DATA = "data"
    KEY_MESSAGE = "message"
    KEY_STATUS = "status"

    def __init__(self, data, message, status):
        self.data = data
        self.message = message
        self.status = status

    def get_json(self):
        return jsonify({
            Response.KEY_DATA: self.data,
            Response.KEY_MESSAGE: self.message,
            Response.KEY_STATUS: self.status
        })