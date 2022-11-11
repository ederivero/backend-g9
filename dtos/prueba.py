from marshmallow import Schema, fields

# DTO (Data Transfer Object - Objectos de Transferencia de Datos) Manual
class PruebaDto(Schema):
    # https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html?highlight=fields#module-marshmallow.fields
    id = fields.Int()
    nombre = fields.Str(required=True, error_messages={'required': 'Este campo es obligatorio'})
    correo = fields.Email(error_messages={'invalid': 'Correo electronico invalido'})
