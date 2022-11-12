from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.tareas import TareaModel

class TareaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = TareaModel
        # cuando nosotros creamos un DTO este solamente servira para las columnas de ese modelo PERO sin ninguna llave foranea
        # si queremos utilizar tambien las llaves foraneas:
        include_fk = True