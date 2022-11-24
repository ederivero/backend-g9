from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .serializers import PruebaSerializer, DepartamentoSerializer, AlmacenSerializer
from .models import DepartamentoModel, AlmacenModel

# request > es la informacion que me llega desde el client
# https://www.django-rest-framework.org/api-guide/views/#api_view
@api_view(http_method_names=['GET', 'POST'])
def saludar(request: Request):
    # request.data > es el cuerpo (body) que me envia el cliente
    print(request.data)
    # es la informacion enviada por la URL pero en formato de llave=valor
    print(request.query_params)
    if request.method == 'GET':
        return Response(data={
            'message': 'Bienvenido a mi API'
        }, status=200)
        
    elif request.method == 'POST':
        body = request.data
        nombre = body.get('nombre')
        # en base al nombre que vamos a recibir por el body en vez de que diga 
        return Response(data={
            'message': f'Hola {nombre}'
        })

@api_view(http_method_names=['GET'])
def parametros(request:Request, nombre):
    print(nombre)
    
    return Response(data={
        'message': 'Bienvenido al endpoint de parametros'
    })

class PruebaApiView(ListCreateAPIView):
    # vistas genericas me piden dos atributos  sirven para trabajar con modelos de la base de datos, no se suele trabajar con informacion aislada 
    # serializer_class > DTO que convertia la informacion entrante a tipos de datos conocidos por python y convertia la informacion saliente a tipos de datos conocidos por los JSON
    serializer_class = PruebaSerializer
    # queryset > La informacion que vamos a extraer de nuestra base de datos
    queryset = [{
        'nombre':'Eduardo',
        'apellido': 'De Rivero'
    },{
        'nombre': 'Raul',
        'apellido': 'Martinez'
    }, {
        'nombre': 'Ximena',
        'apellido': 'Recabarren'
    }]

    def post(self, request: Request):
        print(request.data)
        body = request.data
        serializador = PruebaSerializer(data=body)
        dataValida = serializador.is_valid()

        if not dataValida:
            return Response(data={
                'message': 'Data incorrecta',
                # error > mostrara los errores del porque la data es invalida
                'content': serializador.errors
            })
        else:
            # validated_data > mostrara la data ya validad, osea ya pasada por el filtro del serializado
            print(serializador.validated_data)
            self.queryset.append(serializador.validated_data)
            
            return Response(data={
                'message': 'Usuario agregado exitosamente'
            }, status=status.HTTP_201_CREATED)


class DepartamentosApiView(ListCreateAPIView):
    serializer_class = DepartamentoSerializer
    # SELECT * FROM departamentos;
    queryset = DepartamentoModel.objects.all()

class DepartamentoApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = DepartamentoSerializer
    queryset = DepartamentoModel.objects.all()


# TODO: Realizar el crud pero ahora con los almacenes
class AlmacenesApiView(ListCreateAPIView):
    serializer_class = AlmacenSerializer
    queryset = AlmacenModel.objects.all()

class AlmacenApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AlmacenSerializer
    queryset = AlmacenModel.objects.all()