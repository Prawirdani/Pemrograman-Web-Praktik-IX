# file routes.py untuk definisi rute atau alamat yang tersedia pada rest api

from app import app
from app.controller import UserController
from flask import request


@app.route("/")
def index():
    return "hello world"


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return UserController.index()
    elif request.method == "POST":
        return UserController.store()


@app.route("/users/<id>", methods=["GET", "PUT", "DELETE"])
def user_by_id(id):
    if request.method == "GET":
        return UserController.show(id)
    elif request.method == "PUT":
        return UserController.update(id)
    elif request.method == "DELETE":
        return UserController.delete(id)
