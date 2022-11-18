from django.db import models

class DepartamentoModel(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/
    # declaramos las columnas de este modelo
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    # si nosotros no declaramos el Autofield Django de manera predeterminada creara una columna llamada 'id' que sea autoincrementable 
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-options > mostrarme todas las opciones que le puedo colocar a todas las columnas
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    codigoPostal = models.CharField(max_length=10, unique=True, db_column='codigo_postal')

    class Meta:
        # pasarle metadata o informacion adicional a la clase de la cual estamos heredando
        # https://docs.djangoproject.com/en/4.1/ref/models/options/
        db_table = 'departamentos'

class AlmacenModel(models.Model):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#choices
    # se declara una lista de tuplas en la cual el primer valor de cada tupla sera lo que se guardara en la base de datos, mientras que el segundo valor sera lo que el usuario leera al devolver la informacion
    # UTILIZANDO UNA LISTA DE TUPLAS
    tipoAlmacen = [
        ('A','SECO'), 
        ('B','SEMI-SECO'), 
        ('C', 'HUMEDO')
        ]

    # FORMA UTILIZANDO CLASES
    class TipoAlmacenOpciones(models.TextChoices):
        SECO = ('A','SECO')
        SEMISECO = ('B','SEMI-SECO')
        HUMEDO = ('C', 'HUMEDO')

    # no voy a crear la columna id
    espacioAnaquel = models.IntegerField(db_column='espacio_anaquel')
    tipo = models.CharField(max_length=100, choices=tipoAlmacen)
    # tipo = models.CharField(max_length=100, choices=TipoAlmacenOpciones.choices)
    direccion = models.TextField()
    # RELACIONES ONE-TO-ONE
    # on_delete > se guardara la informacion de como debe actuar el almacen si es que se elimina el departamento (el registro con ese modelo)
    # CASCADE > se elimina el departamento y en forma de cascada se elimina el almacen
    # PROTECT > evita la eliminacion y lanza un error de tipo ProtectedError
    # RESTRICT > muy similar al PROTECT pero emite un error de tipo RestrictedError
    # SET_NULL > elimina el departamento y a este valor lo cambia a null
    # SET_DEFAULT > elimina el departamento pero tenemos que indicar un valor por default para que le cambie a ese valor
    # DO_NOTHING > elimina el departamento PERO conserva el valor (FK) con lo que genera una mala integridad de informacion, NO USAR ESTE porque malogra la calidad de la data
    departamento = models.OneToOneField(to=DepartamentoModel, on_delete=models.CASCADE, db_column='departamento_id')

    class Meta:
        # db_table > indica como se llamara esta tabla en la base de datos, si no le indicamos usara el nombre de la clase como nombre de la tabla
        db_table = 'almacenes'