# setup/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse

# Importe as ViewSets dos seus aplicativos
from escola.views import AlunosViewSet, CursosViewSet
from usuarios.views import UsuariosViewSet

# Crie um router para a API principal
router = routers.DefaultRouter()
router.register('usuarios', UsuariosViewSet, basename='usuarios')
router.register('escola/cursos', CursosViewSet, basename='cursos')
router.register('escola/alunos', AlunosViewSet, basename='alunos')


# Crie uma view personalizada para a URL raiz (http://localhost:8000/)
class RootAPIView(APIView):
    def get(self, request, format=None):
        return Response({
            # Usa o nome da rota de admin e constrói a URL completa
            'admin': request.build_absolute_uri(reverse('admin:index')),
            # Usa o nome padrão de rota da raiz do router (api-root)
            'api': request.build_absolute_uri(reverse('api-root')),
        })


urlpatterns = [
    # Mapeia a URL raiz para a nova view que retorna os links de API e admin
    path('', RootAPIView.as_view(), name='api-root-redirect'),
    
    path('admin/', admin.site.urls),
    
    # A URL raiz da API (`/api/`) agora lista todas as rotas registradas no router.
    # O router do Django REST Framework já faz o trabalho de criar a página principal da API.
    # O nome da rota "api-root" é definido aqui automaticamente
    path('api/', include(router.urls)),
    
    # Mantenha as rotas de token-auth separadas, pois não fazem parte do roteador
    path('api-token-auth/', obtain_auth_token),
]
