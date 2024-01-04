# file routes.py untuk definisi rute atau alamat yang tersedia pada rest api

from app import app
from app.controller import UserController, TodoController
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


@app.route("/todos", methods=["GET", "POST"])
def todos():
    if request.method == "GET":
        return TodoController.index()
    elif request.method == "POST":
        return TodoController.store()


@app.route("/todos/<id>", methods=["GET", "PUT", "DELETE"])
def todo_by_id(id):
    if request.method == "GET":
        return TodoController.show(id)
    elif request.method == "PUT":
        return TodoController.update(id)
    elif request.method == "DELETE":
        return TodoController.delete(id)


@app.route("/login", methods=["POST"])
def login():
    return UserController.login()


@app.route("/refresh", methods=["POST"])
def refresh():
    return UserController.refresh()
