from django.urls import path
from .views import *

urlpatterns = [
    path('registro/', RegistroUsuarioApiView.as_view()),
    path('platos/', PlatosApiView.as_view()),
]