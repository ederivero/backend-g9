from flask import Flask
from datetime import datetime

# __name__ > muestra si el archivo es el archivo principal del proyecto, mostrara el valor de '__main__' y si no entonces mostrara otro valor
print(__name__)
app = Flask(__name__)

# Endpoint > es cuando definimos una ruta para que pueda ser accedida
# si no se define que verbo HTTP puede acceder, entonces el valor por defecto sera GET
@app.route('/', methods = ['GET'])
def inicio():
    # Controlador (Controller) > la funcionabilidad que tendra mi endpoint
    print('ingreso al endpoint inicial')
    # Siempre en todo controlador hay que retornar algo
    return 'Bienvenido a mi primera API en Flask semana 2'

@app.route('/estado', methods= ['GET'])
def estado():
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    hora_servidor = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
    return {
        'estado': True,
        'hora': hora_servidor
    }

@app.route('/identificarse', methods= ['POST'])
def identificacion():
    return {
        'message': 'Identificacion registrada exitosamente'
    }

# run > sirve para correr nuestro servidor en modo de desarrollo
# si declaramos algo despues del metodo run este nunca se llamara porque aca se queda 'pegado' esperando peticiones del cliente
# debug > indicara si guardamos algun archivo dentro del proyecto reiniciara automaticamente el servidor
app.run(debug=True)