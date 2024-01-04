from app.model.todo import Todos
from flask import request, jsonify
from app import response, db
from app.controller import UserController
from flask_jwt_extended import jwt_required


# Decorator jwt untuk menandakan bahwa untuk mengakses function ini dibutuhkan access token
@jwt_required()
def index():
    try:
        user_id = request.args.get("user_id")
        todos = Todos.query.filter_by(user_id=user_id).all()
        data = transform(todos)
        return response.ok(data, "Berhasil mengambil data todos berdasarkan user id")
    except Exception as e:
        return response.badRequest(None, "Terjadi kesalahan")


def store():
    try:
        todo = request.json["todo"]
        desc = request.json["desc"]
        user_id = request.json["user_id"]

        newTodo = Todos(todo=todo, description=desc, user_id=user_id)
        db.session.add(newTodo)
        db.session.commit()

        return response.ok(None, "Berhasil membuat todo")
    except Exception as e:
        return response.badRequest(None, "Terjadi kesalahan")


def update(id):
    try:
        # Ambil nilai baru yang ingin diubah
        todo = request.json["todo"]
        desc = request.json["desc"]

        # Cari data todo berdasarkan id todo pada database
        data_todo = Todos.query.filter_by(id=id).first()
        if not data_todo:
            return response.badRequest(None, "Todo tidak ditemukan")

        # Ganti nilai todo dan description dengan data yang di input dari request body
        data_todo.todo = todo
        data_todo.description = desc
        db.session.commit()

        return response.ok(None, "Berhasil update todo")
    except Exception as e:
        return response.badRequest(None, "Terjadi kesalahan")


def show(id):
    try:
        data_todo = Todos.query.filter_by(id=id).first()
        if not data_todo:
            return response.badRequest(None, "Todo tidak ditemukan")

        data = singleTransform(data_todo)
        return response.ok(data, "Berhasil mengambil data todo berdasarkan id")
    except Exception as e:
        return response.badRequest(None, "Terjadi kesalahan")


def delete(id):
    try:
        # Cari data todo berdasarkan id pada database
        data_todo = Todos.query.filter_by(id=id).first()

        # Return Bad Request Jika todo tidak ditemukan
        if not data_todo:
            return response.badRequest(None, "Todo tidak ditemukan")

        # hapus data todo
        db.session.delete(data_todo)

        # commit / simpan perubahan
        db.session.commit()

        return response.ok(None, "Berhasil menghapus todo")
    except Exception as e:
        return response.badRequest(None, "Terjadi kesalahan")


def singleTransform(data_todo):
    data = {
        "id": data_todo.id,
        "user_id": data_todo.user_id,
        "todo": data_todo.todo,
        "description": data_todo.description,
        "created_at": data_todo.created_at,
        "updated_at": data_todo.updated_at,
        "users": UserController.singleTransform(data_todo.users),
    }
    return data


def transform(todos):
    array = []
    for todo in todos:
        array.append(singleTransform(todo))
    return array
