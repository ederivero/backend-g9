from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.regalo import RegaloModel

class RegaloDto(SQLAlchemyAutoSchema):
    class Meta:
        model = RegaloModel