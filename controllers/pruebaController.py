from flask_restful import Resource, request
from marshmallow.exceptions import ValidationError
from dtos.prueba import PruebaDto

class PruebaController(Resource):
    def post(self):
        try:
            data= request.get_json()
            validador = PruebaDto()
            # cargar la informacion a validar
            dataValidada = validador.load(data)
            print(dataValidada)

            return{
                'message':'ok'
            }
        # Si al momento de hacer la validacion de nuestro DTO falla algun atributo entonces el propio marshmallow emitira un error que lo podremos capturar mediante el except de ValidationError
        except ValidationError as error:
            # args > el atributo donde se almacenara toda la descripcion de los errores
            return{
                'message':'Error al hacer la consulta',
                'content': error.args
            }
