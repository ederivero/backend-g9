from .models import UsuarioModel, PlatoModel
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):

    def save(self):
        # es el que se encarga de guardar el registro en la base de datos
        # 1. Crea la instancia de nuestro nuevo usuario

        # self.validated_data = {
        #     'nombre': 'Eduardo',
        #     'apellido': 'de Rivero',
        #     # ...
        # }
        # nuevoUsuario = UsuarioModel(
        #     nombre = self.validated_data.get('nombre'), 
        #     apellido = self.validated_data.get('apellido')
        #     )

        nuevoUsuario = UsuarioModel(**self.validated_data)

        # 2. genero el hash de la password
        nuevoUsuario.set_password(self.validated_data.get('password'))

        # 3. guardamos el usuario en la base de datos
        nuevoUsuario.save()

        return nuevoUsuario
    class Meta:
        fields = '__all__'
        # exclude = ['correo']
        model = UsuarioModel
        # https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments
        # Definimos un nuevo atributo llamado extra_kwargs en el cual se realiza mediante un diccionario y se utilizara para indicar parametros adicionales a nuestras columnas 
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'id': {
                'read_only': True
            }
        }
        # Con la anterior configuracion estamos indicando que el atributo 'password' solamente sera para escribir mas no para devolver (read) y mientras que el 'id' sera solamente para la lectura, mas nunca se podra utilizara para la escritura (write)


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        fields = '__all__'