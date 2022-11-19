# Aca definiremos todas las rutas que tendra acceso nuestra aplicacion
# Listado de los anexos de esta aplicacion
from django.urls import path
from .views import saludar, parametros, PruebaApiView, DepartamentosApiView, DepartamentoApiView

# Tenemos que crear esta variable NO SE PUEDE LLAMAR DE OTRA MANERA
urlpatterns = [
    # todas las rutas no pueden comenzar con slash '/' 
    path('inicio/', saludar),
    path('parametros/<str:nombre>', parametros),
    # el metodo as_view convierte la clase en una vista para que pueda ser consumida por Django
    path('prueba/', PruebaApiView.as_view()),
    path('departamentos/', DepartamentosApiView.as_view()),
    path('departamento/<int:pk>', DepartamentoApiView.as_view()),

]