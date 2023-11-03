from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

# Konfigurasi alamat ke database
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flask_latihan"  # Sesuaikan dengan nama database yang dibuat

# Inisiasi MySQL ke Flask
mysql = MySQL(app)


@app.route("/")  # rute alamat "localhost:5000/"
def index():
    # Cursor mysql
    cur = mysql.connection.cursor()

    # Eksekusi kueri
    cur.execute("SELECT * FROM users")

    # Tampung seluruh data dari kueri yang dieksekusi
    users = cur.fetchall()

    # Tutup Koneksi
    cur.close()

    # masukkan data users kedalam dictionary data
    data = {"title": "Home", "users": users}

    # Render file index.html beserta data
    return render_template("index.html", data=data)


@app.route("/about")  # rute alamat "localhost:5000/about"
def about():
    return render_template("about.html")  # Render file about.html


if __name__ == "__main__":
    app.run(debug=True)
