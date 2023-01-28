from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/operaciones', methods = ["GET", "POST"])
def operaciones():
    if(request.method == "POST"):
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        opera = request.form.get("opera")

        if(opera == "suma"):
            return "<h1> la suma es: {} </h1>".format(str(int(num1) + int(num2)))
        elif(opera == "resta"):
            return "<h1> la resta es: {} </h1>".format(str(int(num1) - int(num2)))
        elif(opera == "multiplicacion"):
            return "<h1> la multiplicación es: {} </h1>".format(str(int(num1) * int(num2)))
        elif(opera == "division"):
            return "<h1> la división es: {} </h1>".format(str(int(num1) / int(num2)))
    else:
        return'''
            <form action = "/operaciones" method = "POST">
            <label>Suma: </label>
            <input type = "radio" name = "opera" value = "suma"/></br></br>
            <label>Resta: </label>
            <input type = "radio" name = "opera" value = "resta"/></br></br>
            <label>Multiplicación: </label>
            <input type = "radio" name = "opera" value = "multiplicacion"/></br></br>
            <label>Division: </label>
            <input type = "radio" name = "opera" value = "division"/></br></br>
            <label>N1: </label>
            <input type = "text" name = "num1"/></br></br>
            <label>N2: </label>
            <input type = "text" name = "num2"/></br></br>
            <input type = "submit" value = "Calcular"/>
            </form>
        '''


if __name__ == "__main__":
    app.run(debug = True, port = 8080)