from rest_framework import serializers

# https://www.django-rest-framework.org/api-guide/serializers/
class PruebaSerializer(serializers.Serializer):
    # un serializador es el que transfomara la info entrante y saliente
    # https://www.django-rest-framework.org/api-guide/fields/#charfield
    nombre = serializers.CharField(max_length = 40, allow_null=False)
    apellido = serializers.CharField(allow_null=False)