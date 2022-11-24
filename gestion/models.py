from django.db import models
# contrib > contributions 
# auth_user se encuentra en la aplicacion de auth
# AbstractBaseUser > me permite total control sobre la tabla 'auth_user'
# AbstractUser > me permite control solamente en las columnas de nombre, apellido, correo y password de la tabla 'auth_user'
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .authManager import UsuarioManager

# Create your models here.
class PlatoModel(models.Model):
    id = models.AutoField(primary_key= True, null=False, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    # DecimalField > me permite un mejor manejo de la parte entera y parte decimal
    # FloatField > se utilizar un tipo de dato nativo de python que seria el float
    precio = models.DecimalField(max_digits=5, decimal_places=1, null=False)
    disponibilidad = models.BooleanField(default=True)
    # auto_now_add > datetime y sirve para indicar que se guarde la hora y fecha actual del servidor cuando se cree un nuevo registro
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#datefield
    fechaCreacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    
    class Meta:
        db_table = 'platos'
        # ordenar por el precio descendiente
        ordering = ['-precio']


class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    # PermissionsMixin > Me sirve para poder modificar los permisos que tendra este usuario al momento de crearse por los comandos (python manage.py createsuperuser)
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    # xxxxxxxx@xxxxxx.xxx
    correo = models.EmailField(max_length=50, unique=True, null=False)
    password = models.TextField(null=False)
    tipoUsuario = models.CharField(max_length=40, choices=[
        ('ADMIN', 'ADMINISTRADOR'), 
        ('USER', 'USUARIO')
        ], db_column='tipo_usuario')

    objects = UsuarioManager()