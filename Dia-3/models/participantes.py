# Las tablas que originalmente las creamos en la base de datos directamente, ahora se crearan en forma de clases y cada atributo sera una columna de esa tabla
from config import conexion
from sqlalchemy import Column, types
# asi seria si queremos utilizar un tipo de dato de una bd en especifico
# from sqlalchemy.dialects.mysql import JSON

class ParticipanteModel(conexion.Model):
    # Ahora esta clase tendra un comportamiento como si fuera una tabla, es decir todos sus atributos formaran columnas
    # https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
    # https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-camelcase-types
    id = Column(type_= types.Integer, autoincrement= True, primary_key= True)
    nombre = Column(type_= types.String(length=45), nullable= False)
    apellido = Column(type_= types.String(length=50), nullable= False)

    # https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html#orm-declarative-table-configuration
    # con el atributo __tablename__ sirve para indicar como se llamara esta table en la base de datos
    __tablename__ = 'participantes'