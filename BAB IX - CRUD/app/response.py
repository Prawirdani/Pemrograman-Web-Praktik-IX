from flask import jsonify, make_response

# Helper function untuk membuat response dalam format JSON


def ok(value, message):
    res = {"values": value, "message": message}
    return make_response(jsonify(res), 200)


def badRequest(value, message):
    res = {"values": value, "message": message}
    return make_response(jsonify(res), 400)
