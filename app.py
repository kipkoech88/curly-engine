from flask import Flask, make_response, redirect, abort, render_template
#from flask.ext.script import Manager
app = Flask(__name__)
#manager = Manager(app)

@app.route("/")
def home():
    response = make_response("<h2>This documents stores cookies</h2>")
    response.set_cookie("age", "23")
    return render_template("home.html")

@app.route("/actuary")
def index():
    return redirect("https://codingactuary.netlify.app")

@app.route("/user/<id>")
def get_user(id):
    user = int(id)
    if not user:
        abort(502)
    return "<h1>Hello %d</h1>" % user

@app.route("/name/<name>")
def get_name(name):
    if not name:
        abort(404)
    return render_template("user.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)