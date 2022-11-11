from flask import Flask
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from flask_restful import Api

from config import conexion
from models.usuarios import UsuarioModel
from models.tareas import TareaModel
from controllers.usuarioController import UsuariosController
from controllers.pruebaController import PruebaController

# Para cargar las variables del archivo .env para que puedan ser utilizadas como variables de entorno
load_dotenv()

app = Flask(__name__)

# Aca inicializamos la clase Api que nos servira para poder utilizar todos los controladores dentro de la aplicacion de Flask
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

# Inicializamos la instancia de Flask-SQLAlchemy con las propiedades seteadas en la aplicacion de Flask
conexion.init_app(app)

# Inicializamos la clase Migrate con la configuracion de nuestra base de datos y aplicacion de Flask
migrate = Migrate(app, conexion)

# Declarar todas las rutas que vamos a utilizar mediante los controladores
api.add_resource(UsuariosController, '/usuarios')
api.add_resource(PruebaController, '/prueba')

if __name__ == '__main__':
    app.run(debug=True)