# projeto/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui todas as rotas do app 'escola' sob o prefixo 'api/escola/'
    path('api/escola/', include('escola.urls')),
    # Inclui todas as rotas do app 'usuario' sob o prefixo 'api/usuarios/'
    path('api/usuarios/', include('usuarios.urls')),
    # Esta rota pode ficar aqui, pois é uma exceção da API principal
    path('api-token-auth/', obtain_auth_token),
]