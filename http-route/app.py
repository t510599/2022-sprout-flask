from flask import Flask, request, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "<h1>Hello, World!</h1>"

@app.route("/hello")
def hello():
    param = request.args
    if param.get("name"):
        return f"<h1>Hello, {param['name']}!</h1>"

    return "<h1>Hello, <ruby>(　　)<rt>NO NAME</rt></ruby>!</h1>"

@app.route("/get")
def get():
    return request.args

@app.route("/card", defaults={ "name": "???" })
@app.route("/card/<name>")
def card(name):
    return f"<h1>This is card for {name}!</h1>" + \
            "<p>Welcome to sprout!</p>"

@app.route("/echo", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return f"""
            <form action="{url_for('form')}" method="POST">
                <input type="text" name="message">
                <input type="submit" value="submit">
            </form>
        """
    elif request.method == "POST":
        return request.form.get("message")

if __name__ == "__main__":
    app.run(debug=True)