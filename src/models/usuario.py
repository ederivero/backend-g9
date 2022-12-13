from config import conexion
from sqlalchemy import Column, types

class UsuarioModel(conexion.Model):
    id = Column(type_= types.Integer, primary_key= True, unique=True, autoincrement=True)

    nombre = Column(type_=types.String(length=50), nullable=False)
    apellido = Column(type_=types.String(length=50), nullable= False)
    dni = Column(type_=types.String(length=8), unique=True, nullable=False)
    correo = Column(type_=types.String(length=100), unique=True, nullable=False)
    password = Column(type_=types.Text, nullable=False)

    __tablename__ = 'usuarios'