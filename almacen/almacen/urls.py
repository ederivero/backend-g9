# Seria como la guia telefonica entera de todo nuestro proyecto
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # incluimos todas las rutas definidas en el archivo urls de la APLICACION en nuestro proyecto
    path('gestion/', include('gestion.urls'))
]
