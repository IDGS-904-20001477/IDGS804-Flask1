import math
from flask import Flask, render_template
from flask import request

app = Flask(__name__)
@app.route('/cine')
def puntos():
    return render_template("boletos.html")

@app.route('/ticket', methods = ['POST'])
def distancia():
    nombre = request.form.get("txtNombre")
    compradores = int(request.form.get("txtCompradores"))
    cantidad = int(request.form.get("txtCantidad"))
    tarjeta = request.form.get("Tarjeta")
    pago = 0
    boletos = compradores * 7
    if(cantidad <= boletos):
        if(cantidad > 5):
            subtotal = ((cantidad * 12) * 0.15)
            pago = (cantidad * 12) - subtotal
        elif(cantidad >= 3 & cantidad <= 5):
            subtotal = ((cantidad * 12) * 0.10)
            pago = (cantidad * 12) - subtotal
        if(cantidad <= 2):
            pago = cantidad * 12
    else:
        return "Maximo 7 boletos por persona"

    if(tarjeta == "SI"):
        pago = (pago - (pago * 0.10))

    return render_template("ticket.html", cantidad = cantidad, nombre = nombre, pago = pago)


if __name__ == "__main__":
    app.run(debug = True, port = 8080)