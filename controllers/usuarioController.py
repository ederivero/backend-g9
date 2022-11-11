from flask_restful import Resource, request
from config import conexion
from models.usuarios import UsuarioModel

class UsuariosController(Resource):
    # los metodos que nosotros queramos utilizar (GET, POST) lo tendremos que definir como metodo de la clase
    def get(self):
        # https://docs.sqlalchemy.org/en/14/orm/query.html#query-api
        # SELECT * FROM usuarios;
        # me devolvera una lista con todas las instancias de la clase UsuarioModel pero las tengo que formatear para poder devolverlas al frontend
        usuarios = conexion.session.query(UsuarioModel).all()
        print(usuarios)
        print(usuarios[0].nombre)
        # hacer un for en el cual se iteren todos los usuarios y cada usuario convertirlo a un diccionario que tenga el siguiente formato

        # y luego agregarlo a la lista
        usuariosFinales = []
        for usuario in usuarios:
            usuarioDiccionario = {
                'id': usuario.id,
                'nombre': usuario.nombre,
                'correo': usuario.correo,
                'telefono': usuario.telefono
            }
            usuariosFinales.append(usuarioDiccionario)

        return {
            'message': 'Los usuarios son:',
            'content': usuariosFinales
        }
    
    def post(self):
        body = request.get_json()
        try:
            # Primero creo una nueva instancia de mi clase model
            
            nuevoUsuario = UsuarioModel()
            # asigno los valores a los atributos provenientes del body
            # INSERT INTO usuarios (nombre, correo, telefono) VALUES ('...', '...', '...');
            nuevoUsuario.correo = body.get('correo')
            nuevoUsuario.nombre = body.get('nombre')
            nuevoUsuario.telefono = body.get('telefono')

            # ahora agregamos a la base de datos ese nuevo registro creado en base a la instancia
            conexion.session.add(nuevoUsuario)
            # guardar de manera permanente la informacion agregada al nuevo usuario
            conexion.session.commit()
            print(body)
            return {
                'message': 'Usuario creado exitosamente'
            }
        except Exception as error:
            print(error)
            return {
                'message': 'Error al crear el usuario'
            }
