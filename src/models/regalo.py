from config import conexion
from sqlalchemy import Column, types, orm
from sqlalchemy.sql.schema import ForeignKey

class RegaloModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)

    nombre = Column(type_=types.String(length=100), nullable=False)
    url = Column(type_=types.String(100), nullable=True)

    usuarioId = Column(ForeignKey(column='usuarios.id'), type_=types.Integer, nullable=False, name='usuario_id')

    # relationships
    # sirve para poder acceder desde la tabla de la cual se esta creando la FK hacia esta tabla 
    # este atributo no modifica en nada el funcionamiento en la base de datos, es netamente para uso de flask
    # backref > es un atributo VIRTUAL que se creara en el otro modelo (en usuarioModel) y con este atributo se podra acceder a todos los regalos
    usuario = orm.relationship('UsuarioModel', backref = 'regalos')

    __tablename__='regalos'