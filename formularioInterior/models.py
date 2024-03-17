
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):

    nomeUsuario = models.CharField(max_length=100)
    cpfUsuario = models.CharField(max_length=14, unique=True, null=False, blank=False)
    emailUsuario = models.CharField(max_length=100)
    senhaUsuario = models.CharField(max_length=10)
    codUsuario = models.AutoField(primary_key=True, null=False, blank=False)
    USERNAME_FIELD = 'codUsuario'
    def __str__(self):
        return self.nomeUsuario

    def setar_senhaUsuario(self, senha_plana):
        self.senhaUsuario = make_password(senha_plana)

class Hospital(models.Model):
    nomeHospital = models.CharField(max_length=100)
    codHospital = models.AutoField(primary_key=True, null=False, blank=False)
    sn_interior = models.CharField(max_length=1)
    
    def __str__(self):
        return self.nomeHospital
    
    
class Cidade(models.Model):
    nomeCidade = models.CharField(max_length=50)
    codCidade = models.AutoField(primary_key=True)
    def __str__(self):
        return self.nomeCidade