from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  # rute alamat "localhost:5000/"
def index():
    data = {"title":"Home", "nama":"John doe"}
    return render_template("index.html", data=data) # Render file index.html beserta data



@app.route("/about")  # rute alamat "localhost:5000/about"
def about():
    return render_template("about.html") # Render file about.html


if __name__ == "__main__":
    app.run(debug=True)

