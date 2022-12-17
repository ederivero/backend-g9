from marshmallow import Schema, fields

class LoginDto(Schema):
    correo = fields.Email(required=True)
    password = fields.Str(required=True)