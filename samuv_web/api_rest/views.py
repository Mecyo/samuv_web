from django.shortcuts import render
from samuv_web import models
import pytz
from datetime import datetime
from api_rest import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

class LoginServiceView(APIView):

    def post(self, request, format=None):
        userName =  request.data.get('login')
        password = request.data.get('senha')
        if "@" in userName:
            usuario =  models.Usuario.objects.get(email=userName, senha=password)
        if "@" not in userName:
            usuario =  models.Usuario.objects.get(login=userName, senha=password)
        serializer = serializers.UsuarioSerializer(usuario)
        return Response(serializer.data)
		

class IniciarAtendimentoServiceView(APIView):
	
    def post(self, request):
        now = datetime.utcnow().replace(tzinfo=pytz.UTC)
        profissional_id = request.data.get('profissional_id')
        Profissional = models.Profissional.objects.get(idProfissional=profissional_id)
        paciente_id = request.data.get('paciente_id')
        Paciente = models.Paciente.objects.get(idPaciente=paciente_id)
        Doenca = models.Doenca.objects.create(idPaciente=Paciente,)	
		
        novoAtendimento = models.Atendimento.objects.create(idProfissional=Profissional, idDoenca=Doenca, dataHora=now)
		
        Imagem = models.Imagem.objects.create(idAtendimento=novoAtendimento)
        image_file = request.data.get('image')
        Imagem.foto.save(image_file)
		
        Ferida = models.Ferida.objects.create(idDoenca=Doenca.idDoenca)
		
        Caracteristica = ProcessarImagem(Ferida.idFerida, Imagem)
        
        novoAtendimento.idCaracteristica = Caracteristica.idCaracteristica

        novoAtendimento.save()
		
        serializer = serializers.AtendimentoSerializer(novoAtendimento)
        return Response(serializer.data)

		
class ImagemServiceView(APIView):

    def post(self, request, format=None):
        profissional = models.Profissional.objects.get(request.data.get('idProfissional'))
        paciente = models.Paciente.objects.get(request.data.get('idPaciente'))
        atendimento = models.Atendimento.objects.get(request.data.get('idAtendimento'))
        imagem = models.Imagem.objects.filter(idAtendimento=atendimento)
        serializer = serializers.ImagemSerializer(imagem)
        return Response(serializer.data)