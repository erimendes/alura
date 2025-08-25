# usuarios/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Importe os seus outros arquivos
from .serializers import UsuariosSerializer
from .models import PerfilUsuario

class UsuariosViewSet(viewsets.ModelViewSet):
    """
    API de usuários para criação e leitura.
    """
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer

    def create(self, request, *args, **kwargs):
        print("Dados recebidos para cadastro:")
        print(request.data)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class LoginView(APIView):
    """
    API para autenticação de usuário e obtenção de token.
    """
    def post(self, request, *args, **kwargs):
        # 1. Obter os dados de login da requisição
        username = request.data.get('username')
        password = request.data.get('password')

        # 2. Autenticar o usuário
        user = authenticate(username=username, password=password)

        if user:
            # 3. Se o usuário for válido, obter ou criar um token
            token, created = Token.objects.get_or_create(user=user)
            
            # 4. Retornar uma resposta de sucesso com o token e dados do usuário
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
            })
        else:
            # 5. Se as credenciais forem inválidas, retornar um erro
            return Response(
                {'error': 'Credenciais inválidas'},
                status=status.HTTP_400_BAD_REQUEST
            )
