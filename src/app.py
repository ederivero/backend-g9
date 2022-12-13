from flask import Flask
from os import environ
from flask_migrate import Migrate
from config import conexion
# declaramos los modelos para que el historia de migraciones lo registre
from models.usuario import UsuarioModel
from models.intercambio import IntercambioModel
from models.regalo import RegaloModel
# Para utilizar las variables declaradas en el archivo .env como variables de entorno
from dotenv import load_dotenv
load_dotenv()

aplicacion = Flask(__name__)

# Variable que utiliza sqlalchemy para poder conectarse a la base de datos
aplicacion.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

# inicializamos la conexion utilizando la variable seteada previamente
conexion.init_app(app=aplicacion)

# comenzamos a utilizar las migraciones
Migrate(app=aplicacion, db=conexion)





if __name__ == '__main__':
    aplicacion.run(debug=True)