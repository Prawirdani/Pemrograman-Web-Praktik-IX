from flask import Flask

app = Flask(__name__)


@app.route("/")  # rute alamat "localhost:5000/"
def index():
    return "Ini halaman home"


@app.route("/about")  # rute alamat "localhost:5000/about"
def about():
    return "Ini halaman about"


if __name__ == "__main__":
    app.run(debug=True)
