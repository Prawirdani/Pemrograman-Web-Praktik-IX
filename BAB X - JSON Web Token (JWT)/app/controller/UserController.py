from app.model.user import Users
from app import response, app, db
from flask import request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from datetime import timedelta


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
        # Mengambil nilai name, email dan password dari request body (json)
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
        # Mengambil nilai name, email dan password baru dari request body (json)
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


def login():
    try:
        # Mengambil data email dan password dari request body
        email = request.json["email"]
        password = request.json["password"]

        user = Users.query.filter_by(email=email).first()
        if not user:
            return response.badRequest(None, "User/email tidak terdaftar")

        # Pengecekan password yang di input dari request body dengan password di database yang telah dihash.
        if not user.checkPassword(password):
            return response.badRequest(None, "Password anda salah")

        data = singleTransform(user)

        # Konfigurasi masa expired access token dan refresh token
        expires_access_token = timedelta(days=1)  # 1 Hari
        expires_refresh_token = timedelta(days=3)  # 3 Hari

        # Pembuatan access token
        access_token = create_access_token(
            data, fresh=True, expires_delta=expires_access_token
        )

        # Pembuatan refresh token
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh_token)

        return response.ok(
            {
                "data": data,
                "access_token": access_token,
                "refresh_token": refresh_token,
            },
            "Berhasil login",
        )
    except Exception as e:
        return response.badRequest(None, "Terjadi kesalahan")


# Decorator jwt untuk menandakan bahwa untuk mengakses function ini dibutuhkan refresh token
@jwt_required(refresh=True)
def refresh():
    try:
        # Mengekstrak data user yang terdapat di dalam payload refresh token
        user = get_jwt_identity()

        # membuat access token baru dengan data user yang telah di ekstrak.
        new_access_token = create_access_token(identity=user, fresh=False)

        return response.ok(
            {"access_token": new_access_token}, "Berhasil merefresh token"
        )
    except Exception as e:
        return response.badRequest(None, "Gagal merefresh token")


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
