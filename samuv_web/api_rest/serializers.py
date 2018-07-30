import os
from django.conf import settings
from rest_framework import serializers
from samuv_web import models


class UsuarioSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Usuario
		fields = ('idUsuario', 'nomeUsuario', 'email')
		depth = 1
		

class ProfissionalSerializer(serializers.ModelSerializer):
	
	Usuario = UsuarioSerializer()
	class Meta:
		model = models.Profissional
		fields = ('idProfissional', 'Usuario')
		depth = 1
		
			
class TecnicaSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = models.Tecnica
		fields = ('idTecnica', 'nomeTecnica')
		depth = 1
		

class PacienteSerializer(serializers.ModelSerializer):
	
	Usuario = UsuarioSerializer()
	class Meta:
		model = models.Paciente
		fields = ('idPaciente', 'Usuario')
		depth = 1
		
	
class DoencaSerializer(serializers.ModelSerializer):
	
	Paciente = PacienteSerializer()
	class Meta:
		model = models.Doenca
		fields = ('idDoenca', 'Paciente', 'tipo', 'apelido')
		depth = 1
		
		
class FeridaSerializer(serializers.ModelSerializer):
	
	Doenca = DoencaSerializer()
	class Meta:
		model = models.Ferida
		fields = ('idFerida', 'Doenca')
		depth = 1
		
		
class CaracteristicaFeridaSerializer(serializers.ModelSerializer):
	
	Ferida = FeridaSerializer()
	class Meta:
		model = models.Caracteristica_da_ferida
		fields = ('idCaracteristica', 'Ferida', 'area', 'cor',)
		depth = 1


class AtendimentoSerializer(serializers.ModelSerializer):

	Tecnica = TecnicaSerializer()
	Profissional = ProfissionalSerializer()
	Doenca = DoencaSerializer()
	CaracteristicaFerida = CaracteristicaFeridaSerializer()
	class Meta:
		model = models.Atendimento
		fields = ('idAtendimento', 'Tecnica', 'Profissional', 'Doenca', 'CaracteristicaFerida')
		depth = 1


class ImagemSerializer(serializers.HyperlinkedModelSerializer):
	
	Atendimento = AtendimentoSerializer()
	class Meta:
		model = models.Imagem
		fields = ('idImagem', 'Atendimento', 'imageName', 'foto')
		depth = 1
