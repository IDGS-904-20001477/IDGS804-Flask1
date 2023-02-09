from flask import Flask, render_template
from flask import request
from datetime import datetime, date

app = Flask(__name__)
@app.route('/')
def puntos():
    return render_template("examenDatos.html")

@app.route('/datos', methods = ['POST'])
def datos():
    nombre = request.form.get("txtNombre")
    apeP = request.form.get("txtApeP")
    apeM = request.form.get("txtApeM")
    dia = int(request.form.get("txtDia"))
    mes = int(request.form.get("txtMes"))
    año = int(request.form.get("txtAnio"))
    p1 = request.form.get("P1")
    p2 = request.form.get("P2")
    p3 = request.form.get("P3")
    p4 = request.form.get("P4")
    p5 = request.form.get("P5")
    fechaActual = date.today()
    edad = fechaActual.year - año - ((fechaActual.month, fechaActual.day) < (mes, dia))
    signosZodiacales = ['Mono', 'Gallo', 'Perro', 'Cerdo', 'Rata', 'Buey', 'Tigre',
                  'Conejo', 'Dragón', 'Serpiente', 'Caballo', 'Cabra']
    imagenes = {
    "Mono": "https://cdn.pixabay.com/photo/2017/01/18/01/04/vector-1988652_640.png",
    "Gallo": "https://cdn.pixabay.com/photo/2015/12/30/21/45/rooster-1114833_640.jpg",
    "Perro": "https://img2.freepng.es/20180627/gcp/kisspng-dog-chinese-zodiac-astrological-sign-calendar-year-of-the-rooster-5b330dabd3f5a6.1428893415300724918682.jpg",
    "Cerdo": "https://img2.freepng.es/20180702/ie/kisspng-pig-chinese-zodiac-astrological-sign-dog-rooster-5b3a395a934315.2948329615305424266032.jpg",
    "Rata": "https://cdn.pixabay.com/photo/2017/01/18/01/04/vector-1988653_640.png",
    "Buey": "https://cdn.pixabay.com/photo/2017/01/18/01/04/vector-1988651_640.png",
    "Tigre": "https://w1.pngwing.com/pngs/29/284/png-transparent-chinese-new-year-red-chinese-zodiac-tiger-astrological-sign-horoscope-lunar-calendar-aquarius-chinese-dragon.png",
    "Conejo": "https://e7.pngegg.com/pngimages/174/314/png-clipart-rabbit-chinese-zodiac-symbol-chinese-characters-chinese-new-year-rabbit-mammal-animals.png",
    "Dragón": "https://images.vexels.com/media/users/3/282629/isolated/preview/5b4f6600ccbdb881f8870f02419820ec-signo-del-zodiaco-del-draga-n-del-aa-o-nuevo-chino.png",
    "Serpiente": "https://cdn.pixabay.com/photo/2017/01/18/01/04/vector-1988654_640.png",
    "Caballo": "https://cdn.pixabay.com/photo/2017/01/18/01/09/vector-1988659_640.png",
    "Cabra": "https://cdn.pixabay.com/photo/2017/01/18/01/03/vector-1988650_640.png",
    }
    signo = signosZodiacales[(año - 4) % 12]
    imagen = imagenes[signo]

    calificacion = 0
    if(p1 == "argentina"):
        calificacion += 1
    else:
        calificacion
    if(p2 == "cumbia"):
        calificacion += 1
    else:
        calificacion
    if(p3 == "messi"):
        calificacion += 1
    else:
        calificacion
    if(p4 == "nada"):
        calificacion += 1
    else:
        calificacion
    if(p5 == "juan"):
        calificacion += 1
    else:
        calificacion
    
    return render_template("resultadosPreguntas.html", nombre = nombre, apeP = apeP, apeM = apeM, signo = signo, imagen = imagen, edad = edad, calificacion = calificacion)


if __name__ == "__main__":
    app.run(debug = True, port = 8080)