import os
from django.db import models
from datetime import datetime
from django.conf import settings


def get_image_path(filename, instance):
        return os.path.join(settings.IMG_DIR, str(instance.idImagem), filename)
		

class Usuario(models.Model):
    idUsuario= models.AutoField('auth.User', primary_key=True, blank=False, null=False)
    nomeUsuario = models.CharField(max_length=250, blank=True, null=True)
    login = models.CharField(max_length=20, unique=True, blank=False, null=False)
    email = models.CharField(max_length=50, unique=True, blank=False,)
    senha = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nomeUsuario

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Profissional(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
    idProfissional = models.AutoField(primary_key=True, blank=False, null=False)
    
    def __str__(self):
        return self.usuario.nomeUsuario
		
    class Meta:
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"

		
class Paciente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
    idPaciente = models.AutoField(primary_key=True, blank=False, null=False)
    
    def __str__(self):
        return self.usuario.nomeUsuario
	
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"	
		
		
class Doenca(models.Model):
    idDoenca = models.AutoField(primary_key=True, blank=False, null=False)
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,)
    tipo = models.CharField(max_length=250, blank=True, null=True)
    apelido = models.CharField(max_length=50, blank=True, null=True)
		
    class Meta:
        verbose_name = "Doença"
        verbose_name_plural = "Doenças"	
		
	
class Ferida(models.Model):
    idFerida = models.AutoField(primary_key=True, blank=False, null=False)
    idDoenca = models.ForeignKey(Doenca, on_delete=models.CASCADE,)
		
    class Meta:
        verbose_name = "Ferida"
        verbose_name_plural = "Feridas"	
	
	
class Caracteristica_da_ferida(models.Model):
    idCaracteristica = models.AutoField(primary_key=True, blank=False, null=False)
    idFerida = models.ForeignKey(Ferida, on_delete=models.CASCADE,)
    area = models.FloatField(blank=True, null=True)
    cor = models.CharField(max_length=10, blank=True, null=True)
	
    class Meta:
        verbose_name = "Característica da ferida"
        verbose_name_plural = "Características das feridas"
	
	
class Tecnica(models.Model):
    idTecnica = models.AutoField(primary_key=True, blank=False, null=False)
    nomeTecnica = models.CharField(max_length=250, blank=True, null=True)
	
    def __str__(self):
        return self.nomeTecnica
			
    class Meta:
        verbose_name = "Técnica"
        verbose_name_plural = "Técnicas"
	
		
class Atendimento(models.Model):
	idAtendimento = models.AutoField(primary_key=True, blank=False, null=False)
	idTecnica = models.ForeignKey(Tecnica, on_delete=models.CASCADE, blank=True, null=True)
	idProfissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, blank=False, null=False)
	idDoenca = models.ForeignKey(Doenca, on_delete=models.CASCADE, blank=True, null=True)
	idCaracteristica = models.ForeignKey(Caracteristica_da_ferida, on_delete=models.CASCADE, blank=True, null=True)
	dataHora = models.DateTimeField(null=False, blank=False, default=datetime.now())
	

class Imagem(models.Model):
    idImagem = models.AutoField(primary_key=True, blank=False, null=False)
    idAtendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE,)
    imageName = models.CharField(max_length=80, default='IMG' + datetime.now().strftime("%d%m%Y%I%M%S"))
    foto = models.ImageField(imageName, upload_to=settings.IMG_DIR)
    
    def __str__(self):
        return self.imageName
		
    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"
