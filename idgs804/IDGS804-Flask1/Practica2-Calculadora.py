import math
from flask import Flask, render_template
from flask import request

app = Flask(__name__)
@app.route('/puntos')
def puntos():
    return render_template("puntos.html")

@app.route('/distancia', methods = ['POST'])
def distancia():
    x1 = request.form.get("txtX1")
    y1 = request.form.get("txtY1")
    x2 = request.form.get("txtX2")
    y2 = request.form.get("txtY2")
    res = math.sqrt((pow(float(x2) - float(x1), 2) + pow(float(y2) - float(y1), 2)))
    return render_template("distancia.html", res = res)


if __name__ == "__main__":
    app.run(debug = True, port = 8080)