from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi alamat ke database
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flask_latihan"  # Sesuaikan dengan nama database yang dibuat

# Inisiasi MySQL ke Flask
mysql = MySQL(app)

# Session Secret Key
app.secret_key = "INI_RAHASIA"

@app.route("/")  # rute alamat "localhost:5000/"
def index():
    # Jika Session ada di browser client / jika user logged in
    # Maka halaman index akan ditampilkan
    if "is_logged_in" in session:
        # Cursor mysql
        cur = mysql.connection.cursor()

        # Eksekusi kueri
        cur.execute("SELECT * FROM users")

        # Tampung seluruh data dari kueri yang dieksekusi
        users = cur.fetchall()

        # Tutup Koneksi
        cur.close()

        # masukkan data users kedalam dictionary data
        data = {"title": "Home", "username": session["username"], "users": users}

        # Render file index.html beserta data
        return render_template("index.html", data=data)
    else:
        # Jika tidak terdapat session, maka di alihkan ke halaman login
        return redirect(url_for("login"))


@app.route("/about")  # rute alamat "localhost:5000/about"
def about():
    return render_template("about.html")  # Render file about.html

# Rute dan halaman login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Mengambil nilai form dari HTML
        email = request.form['inpEmail']
        password = request.form['inpPass']

        # Cursor mysql
        cur = mysql.connection.cursor()

        # Eksekusi kueri
        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))

        # Tampung data dari kueri yang dieksekusi
        user = cur.fetchone()

        # Tutup Koneksi
        cur.close()

        # Cek apakah terdapat user yang password dan emailnya sesuai di database
        if user:
            # inisiasi session 
            session['is_logged_in'] = True
            session['username'] = user[1]

            # Redirect ke halaman index('/')
            return redirect(url_for("index"))
        else:
            pesanError = "Cek email dan password kamu"
            return render_template("login.html", msg=pesanError)

    else:
        # Jika request method selain POST, maka tampilkan halaman login.html
        return render_template("login.html")

@app.route("/logout")
def logout():
    # Menghapus session
    session.pop("is_logged_in", None)
    session.pop("username", None)

    # Redirect/Alihkan ke halaman login ('/login')
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
