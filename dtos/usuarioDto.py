from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuarios import UsuarioModel

class UsuarioRequestDto(SQLAlchemyAutoSchema):
    # pasar atributos a la clase que estamos heredando
    class Meta:
        # Esta clase permitira definir atributos necesarios para la clase que estamos heredanod
        # model > estaremos indicando a SQLAlchemyAutoSchema cual sera el modelo que tiene que utilizar para generar las validaciones necesarias.
        model = UsuarioModel