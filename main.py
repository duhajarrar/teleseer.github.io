from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
import flask , sqlite3
headers = {'Content-Type': 'text/html'}
app = flask.Flask(__name__)
app.config["DEBUG"] = False

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html")


@app.route('/clients', methods=['GET'])
def clients():
    return render_template("clients.html")

@app.route('/services', methods=['GET'])
def services():
    return render_template("services.html")




app.run()