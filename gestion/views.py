from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioModel, PlatoModel
from .serializers import UsuarioSerializer, PlatoSerializer

class RegistroUsuarioApiView(CreateAPIView):
    queryset = UsuarioModel.objects.all()
    serializer_class= UsuarioSerializer

    def post(self, request: Request):
        informacion = self.serializer_class(data= request.data)
        # donde valida que todos los datos sean correctos
        es_valida = informacion.is_valid()

        if not es_valida:
            return Response(data={
                'message': 'Error al crear el usuario',
                'content': informacion.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Gracias que el serializador es un modelSerializer el metodo save sirve para registrar ese nuevo usuario en la base de datos
            nuevoUsuario = informacion.save()
            # utilizamos el serializador para convertir el nuevo usuario creado a una data legible
            nuevoUsuarioSerializado = self.serializer_class(instance=nuevoUsuario)

            return Response(data={
                'message': 'Usuario creado exitosamente, ya se puede logear',
                # contiene todo el valor del registro pero con sus valores ya registrados en la base de datos
                'content': nuevoUsuarioSerializado.data
            }, status= status.HTTP_201_CREATED)



class PlatosApiView(ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    serializer_class = PlatoSerializer

    def post(self, request:Request):
        data = self.serializer_class(data= request.data)
        # raise_exception > si hay algun error, automaticamente detiene todo el proceso y emite el error
        data.is_valid(raise_exception=True)

        nuevoPlato = data.save()

        return Response(data={
            'message': 'plato creado exitomsamente',
            'content': self.serializer_class(instance=nuevoPlato).data
        })

    def get(self, request: Request):
        pass