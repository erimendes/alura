# usuario/urls.py

from django.urls import path, include
from rest_framework import routers
from usuarios.views import UsuariosViewSet

router = routers.DefaultRouter()
router.register('', UsuariosViewSet) # O nome da rota pode ser vazio aqui

urlpatterns = [
    path('', include(router.urls)),
]