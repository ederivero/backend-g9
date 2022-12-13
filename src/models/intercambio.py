from config import conexion
from sqlalchemy import Column, types, orm
from sqlalchemy.sql.schema import ForeignKey

class IntercambioModel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    angelId = Column(ForeignKey(column='usuarios.id'), type_=types.Integer, nullable=False, name='angel_id', unique=True)

    ahijadoId= Column(ForeignKey(column='usuarios.id'), type_=types.Integer, nullable=False, name='ahijado_id', unique=True)

    # relationships
    # el backref puede ser el mismo nombre siempre y cuando estemos apuntando a diferentes modelos PERO si es al mismo modelo no se puede ya que en la tabla usuarios se creara dos atributos con el mismo nombre 
    # si tenemos dos relaciones iguales se agrega la propiedad foreign_keys (https://docs.sqlalchemy.org/en/14/orm/relationship_api.html#sqlalchemy.orm.relationship.params.foreign_keys) el parametro trabaja o en una lista o un solo elemento
    angel = orm.relationship('UsuarioModel', backref= 'intercambioAngel', foreign_keys = "[IntercambioModel.angelId]")
    ahijado = orm.relationship('UsuarioModel', backref='intercambioAhijado', foreign_keys = "IntercambioModel.ahijadoId")

    __tablename__='intercambios'