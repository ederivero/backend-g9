from flask import Flask, render_template
from flask_mysqldb import MySQL
from os import environ
# sirve para leer el archivo .env y cargar las variables definidas en ese archivo como variables de entorno
from dotenv import load_dotenv

load_dotenv()
# print(environ)

app = Flask(__name__)
# NOTA: Todas las variables de entorno SIEMPRE seran string
# almacena todas las variables de configuracion de la aplicacion de Flask
app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST')  # None
app.config['MYSQL_USER'] = environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = int(environ.get('MYSQL_PORT'))

# print(app.config)
mysql = MySQL(app)


# Un decorador es la forma en la cual nosotros podemos modificar el comportamiento de un metodo de una clase sin la necesidad de modificarlo directamente, es como utilizar la herencia para poder modificar su comportamiento, en este caso, dependientoe de su ruta y su metodos
@app.route('/', methods=['GET'])
def inicio():
    return {
        'message': 'Bienvenido a mi API de colegios'
    }


@app.route('/inicio', methods=['GET'])
def pagina_inicial():
    return render_template('inicio.html')


@app.route('/alumnos', methods=['GET'])
def devolver_alumnos():
    # me crea una conexion con la base de datos
    cursor = mysql.connection.cursor()
    # ejecutamos una clausula hacia una determinada tabla
    cursor.execute("SELECT * FROM alumnos")
    # devolver toda la informacion de esa consulta
    resultado = cursor.fetchall()
    print(resultado)

    return {
        'message': 'Los alumnos son:'
    }


app.run(debug=True)
