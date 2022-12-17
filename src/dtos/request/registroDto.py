from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import validate
from models.usuario import UsuarioModel

class RegistroDto(SQLAlchemyAutoSchema):
    # auto_field() > sirve para modificar un atributo del modelo PERO solo a nivel de DTO (no a nivel de base de datos)
    # https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html
    correo = auto_field(validate=validate.Email(error='El correo ingresado no es un formato valido'), required=True)

    class Meta:
        model = UsuarioModel