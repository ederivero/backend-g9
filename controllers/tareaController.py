from flask_restful import Resource, request
from config import conexion
from models.tareas import TareaModel
from models.usuarios import UsuarioModel
from dtos.tareaDto import TareaRequestDto

class TareasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            serializador = TareaRequestDto()
            dataSerializada = serializador.load(body)
            # buscar si existe el usuario con ese id, si no existe emitir un error indicando que el usuario no existe
            # dataSerializada.get('usuarioId') > esta el usuario
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id= dataSerializada.get('usuarioId')).first()
            # if usuarioEncontrado is None:
            if not usuarioEncontrado:
                raise Exception('Usuario no existe')

            nuevaTarea = TareaModel(**dataSerializada)
            conexion.session.add(nuevaTarea)
            conexion.session.commit()

            return {
                'message': 'Tarea agregada exitosamente'
            }

        except Exception as error:
            return {
                'message': 'Error al crear la tarea',
                'content': error.args
            }

class TareaController(Resource):
    def get(self, usuarioId):
        # Buscar todas las tareas utilizando el usuarioId y luego serializarlas y devoverlas
        tareasEncontradas= conexion.session.query(TareaModel).filter_by(usuarioId= usuarioId).all()
        serializador = TareaRequestDto(many=True)
        
        data = serializador.dump(tareasEncontradas)
        return {
            'message': 'Las tareas son',
            'content': data
        }
