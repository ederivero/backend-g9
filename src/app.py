from flask import Flask
from os import environ
from flask_migrate import Migrate
# Para utilizar las variables declaradas en el archivo .env como variables de entorno
from dotenv import load_dotenv
from flask_restful import Api
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_cors import CORS

from config import conexion
# declaramos los modelos para que el historia de migraciones lo registre
from models.usuario import UsuarioModel
from models.intercambio import IntercambioModel
from models.regalo import RegaloModel
from controllers.usuarioController import RegistroController, LoginController, PerfilController
from controllers.regaloController import RegaloController
load_dotenv()

aplicacion = Flask(__name__)
CORS(app=aplicacion)
api = Api(app=aplicacion)
# Variable que utiliza sqlalchemy para poder conectarse a la base de datos
aplicacion.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

# https://flask-jwt-extended.readthedocs.io/en/stable/options/
aplicacion.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET')
aplicacion.config['JWT_ACCESS_TOKEN_EXPIRES']= timedelta(hours=1, minutes=30)

# Inicializamos nuestra clase JWTManager
JWTManager(app=aplicacion)
# inicializamos la conexion utilizando la variable seteada previamente
conexion.init_app(app=aplicacion)

# comenzamos a utilizar las migraciones
Migrate(app=aplicacion, db=conexion)


# ahora creo mis rutas de mis controladores
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(PerfilController, '/perfil')
api.add_resource(RegaloController, '/regalo')

if __name__ == '__main__':
    aplicacion.run(debug=True)