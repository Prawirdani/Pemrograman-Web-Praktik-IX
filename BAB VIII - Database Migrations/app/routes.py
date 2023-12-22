# file routes.py untuk definisi rute atau alamat yang tersedia pada rest api

from app import app


@app.route("/")
def index():
    return "hello world"
