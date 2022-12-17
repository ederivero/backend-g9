from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.usuario import UsuarioModel

class UsuarioDto(SQLAlchemyAutoSchema):
    # load_only > sirve para indicar que ese atributo solo sera de escritura (cuando ingrese) mas no de lectura (cuando salga)
    # al metodo auto_field adicional a la propiedades que son propias del metodo se le puede pasar los parametros de la configuracion de los Fields de marshmallow
    password = auto_field(load_only=True)
    class Meta:
        model = UsuarioModel