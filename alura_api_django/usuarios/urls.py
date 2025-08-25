# usuario/urls.py

from django.urls import path, include
from rest_framework import routers
from usuarios.views import UsuariosViewSet, LoginView
router = routers.DefaultRouter()
router.register('', UsuariosViewSet) # O nome da rota pode ser vazio aqui

urlpatterns = [
    # A URL para a viewset de usuários
    path('', include(router.urls)),
    
    # A URL para a view de login
    path('login/', LoginView.as_view(), name='login'),
]