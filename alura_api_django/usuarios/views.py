# usuarios/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
# Importe o modelo User
from django.contrib.auth.models import User
from .serializers import UsuariosSerializer

# Classe de depuração
class UsuariosViewSet(viewsets.ModelViewSet):
    """
    API de usuários para criação e leitura.
    """
    # A viewset deve usar o modelo User, não Usuario.
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer

    def create(self, request, *args, **kwargs):
        # Esta linha de print vai mostrar no seu terminal do backend
        # os dados que a API está recebendo do seu frontend.
        print("Dados recebidos para cadastro:")
        print(request.data)
        
        # O resto do código permanece o mesmo.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
