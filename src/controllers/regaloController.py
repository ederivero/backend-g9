from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.regalo import RegaloModel
from config import conexion
from dtos.request.regaloDto import RegaloDto


class RegaloController(Resource):

    @jwt_required()
    def post(self):
        body = request.get_json()
        try:
            data = RegaloDto().load(body)
            usuarioId= get_jwt_identity()
            nuevoRegalo = RegaloModel(**data, usuarioId=usuarioId)
            conexion.session.add(nuevoRegalo)
            conexion.session.commit()

            return {
                'message': 'Regalo creado exitosamente'
            }
        except Exception as e :
            return {
                'message':'Error al crear el regalo',
                'content': e.args
            }

    @jwt_required()
    def get(self):
        usuarioId= get_jwt_identity()
        regalos = conexion.session.query(RegaloModel).filter_by(usuarioId=usuarioId).all()
        resultado = RegaloDto().dump(regalos, many=True)
        return {
            'message': 'los regalos son',
            'content': resultado
        }