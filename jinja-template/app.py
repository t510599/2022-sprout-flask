from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/")
@app.route("/index")
def index():
    return "<h1>It works!</h1>"

@app.route("/hello")
def hello():
    param = request.args
    return render_template("hello.html", name=param.get("name"))

@app.route("/home", defaults={ "name": "Anonymous" })
@app.route("/home/<name>")
def home(name):
    return render_template("home.html", page="Home", name=name)

@app.route("/get")
def get():
    return render_template("get_params.html", items=request.args.items())

@app.route("/echo", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        return request.form.get("message")

if __name__ == "__main__":
    app.run(debug=True)