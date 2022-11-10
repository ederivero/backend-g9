from config import conexion
from sqlalchemy import Column, types

class UsuarioModel(conexion.Model):
    __tablename__='usuarios'

    id = Column(type_ = types.Integer, autoincrement=True, primary_key=True, nullable= False)
    nombre = Column(type_ = types.String(length=45), nullable=False)
    correo = Column(type_ = types.String(length=45), nullable=False, unique=True)
    telefono = Column(type_ = types.String(length=15))