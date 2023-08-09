from flask import Flask, render_template, request

INSTRUMENTS = [
    "Violin",
    "Viola",
    "Cello",
    "Gamba"
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html.j2")

@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html.j2", name=request.form.get("name", "visitor"))

#eventually you might want to unite the three pages into one: "products"
@app.route("/strings")
def strings():
    return render_template("strings.html.j2", instruments=INSTRUMENTS)

@app.route("/bows") 
def bows():
    return render_template("bows.html.j2", instruments=INSTRUMENTS)

@app.route("/impressum")
def about():
    return render_template("impressum.html.j2")

