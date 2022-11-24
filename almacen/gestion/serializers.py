from rest_framework import serializers
from .models import DepartamentoModel, AlmacenModel

# https://www.django-rest-framework.org/api-guide/serializers/
class PruebaSerializer(serializers.Serializer):
    # un serializador es el que transfomara la info entrante y saliente
    # https://www.django-rest-framework.org/api-guide/fields/#charfield
    nombre = serializers.CharField(max_length = 40, allow_null=False)
    apellido = serializers.CharField(allow_null=False)

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentoModel
        fields = '__all__' # ['id', 'nombre'] > Esto solamente usara esas columnas del modelo
        # Si quisiera utilizar todas las columnas exceptuando una o dos (minoria)
        # voy a utilizar todas las columnas menos la columna 'nombre'
        # exclude = ['nombre'] 
        # NOTA: No se usa las dos, o se usa 'fields' o se usa 'exclude'

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlmacenModel
        fields = '__all__'