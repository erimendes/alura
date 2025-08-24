# usuarios/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PerfilUsuario

class UsuariosSerializer(serializers.ModelSerializer):
    # Campos que pertencem ao modelo PerfilUsuario
    endereco = serializers.CharField(max_length=255, required=False)
    complemento = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    cep = serializers.CharField(max_length=9, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'endereco', 'complemento', 'cep']
        extra_kwargs = {'password': {'write_only': True}} # A senha não deve ser retornada em GET

    def create(self, validated_data):
        # Remove os dados do perfil do dicionário para criar o User
        endereco = validated_data.pop('endereco', None)
        complemento = validated_data.pop('complemento', None)
        cep = validated_data.pop('cep', None)
        
        # Cria o objeto User com os dados restantes
        user = User.objects.create_user(**validated_data)

        # Se os dados do perfil existirem, crie o objeto PerfilUsuario
        if endereco:
            PerfilUsuario.objects.create(
                usuario=user,
                endereco=endereco,
                complemento=complemento,
                cep=cep,
            )
        
        return user
