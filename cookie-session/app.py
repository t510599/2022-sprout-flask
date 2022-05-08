from flask import Flask, flash, render_template, request, make_response, url_for, redirect, session
from flask_session import Session

app = Flask(__name__, template_folder="templates")
SESSION_TYPE = "filesystem"
app.config.from_object(__name__)
Session(app)

AccountDB = {
    "admin": "admin",
    "user": "user",
    "sprout": "sprout"
}

@app.route("/")
@app.route("/index")
def index():
    return "<h1>It works!</h1>"

@app.route("/cookie")
def cookie():
    return request.cookies["sprout"]

@app.route("/setcookie")
def setcookie():
    response = make_response(render_template("cookie.html", action="set"))
    response.set_cookie("sprout", "PyLang2022")
    return response

@app.route("/unsetcookie")
def unsetcookie():
    response = make_response(render_template("cookie.html", action="cleared"))
    response.delete_cookie("sprout")
    return response

@app.route("/home")
def home():
    username = session.get("user")
    if not username:
        return redirect(url_for("login"))

    return render_template("home.html", title="Home", name=username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        username = session.get("user")
        if username:
            return redirect(url_for("home"))

        return render_template("login.html", title="Login")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in AccountDB and password == AccountDB[username]:
            session["user"] = username
            return redirect(url_for("home"))
        else:
            flash("Login Failed!")
            return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)