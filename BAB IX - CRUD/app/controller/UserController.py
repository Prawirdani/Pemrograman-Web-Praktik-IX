from app.model.user import Users
from app import response, app, db
from flask import request


def index():
    try:
        users = Users.query.all()  # query mengambil seluruh data users pada database
        data = transform(users)  # konversi ke format dictionary
        return response.ok(data, "Berhasil mengambil data user")
    except Exception as e:
        return response.badRequest(None, "Gagal mengambil data users")


def show(id):
    try:
        user = Users.query.filter_by(id=id).first()

        if not user:  # Jika user tidak ditemukan, maka response BAD REQUEST
            return response.badRequest(None, "Data user tidak ditemukan")

        data = singleTransform(user)
        return response.ok(data, "Berhasil ambil data user berdasarkan id")
    except Exception as e:
        return response.badRequest(None, "Gagal mengambil data users")


def store():
    try:
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]

        user = Users(name=name, email=email)

        # Hash password
        user.setPassword(password)
        # query insert user baru ke database
        db.session.add(user)
        # commit/simpan perubahan
        db.session.commit()

        return response.ok(None, "Berhasil membuat user")
    except Exception as e:
        return response.badRequest(None, "Gagal membuat user")


def update(id):
    try:
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]

        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest(None, "User tidak ditemukan")

        user.name = name
        user.email = email
        user.setPassword(password)
        db.session.commit()

        return response.ok(None, "Berhasil update user")
    except Exception as e:
        return response.badRequest(None, "Gagal update user")


def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest(None, "User tidak ditemukan")

        db.session.delete(user)
        db.session.commit()

        return response.ok(None, "Berhasil hapus user")
    except Exception as e:
        return response.badRequest(None, "Gagal hapus user")


# Helper function untuk mengubah single data tuple dari query database menjadi bentuk dictionary
def singleTransform(user):
    data = {"id": user.id, "name": user.name, "email": user.email}
    return data


# Helper function untuk mengubah  data array tuple dari query database menjadi bentuk array dictionary
def transform(users):
    array = []
    for user in users:
        array.append(singleTransform(user))
    return array
