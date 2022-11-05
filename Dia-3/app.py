from flask import Flask
from config import conexion

app = Flask(__name__)
# Formato para las cadenas de conexion de las base de datos:
# dialecto://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/flask_sqlalchemy'

# configuro mi conexion de sqlalchemy con la aplicacion de flask
conexion.init_app(app)

# indicaremos la creacion de las nuevas tablas que no se encuentren registradas en la base de datos PERO esos modelos tiene que ser utilizado en el proyecto para que se pueda crear la tabla en la bd, emitira un error si no logro conectar a la base de datos
conexion.create_all(app=app)


app.run(debug=True)
