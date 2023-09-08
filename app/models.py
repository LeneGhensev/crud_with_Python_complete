from django.db import models

class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    serie = models.IntegerField()
    nota_final = models.IntegerField()




