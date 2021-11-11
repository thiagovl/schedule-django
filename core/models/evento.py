from datetime import timedelta, timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
import datetime
from datetime import timedelta

# Create your models here.

class Evento(models.Model):
    status_evento = (
        ('P', 'Pendente'),
        ('C', 'Concluído')
    )
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = DateTimeField(verbose_name='DATA DO EVENTO')
    data_criacao = DateTimeField(verbose_name='DATA DE CRIAÇÃO', auto_now=True)
    status = models.CharField(blank=True, null=True, choices=status_evento, max_length=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # chave estrangeira

    # Especificando o nome da tabela
    class Meta:
        db_table = 'evento'

    # Formatando a data
    def get_data_evento(self):
        hs = self.data_evento - datetime.timedelta(hours=3)
        return hs.strftime('%d/%m/%Y %H:%M')

    def get_data_criacao(self):
        hs = self.data_criacao - datetime.timedelta(hours=3)
        return hs.strftime("%d/%m/%Y %H:%M")

    def get_data(self):
        return self.data_evento.strftime('%d')
    
    def get_data_evento_input(self):
        return self.data_evento.strftime('%Y-%m-%d')

    def get_data_evento_input_hora(self):
        hs = self.data_evento - datetime.timedelta(hours=3)
        return hs.strftime("%H:%M")


    def get_mes(self):
        return self.data_evento.strftime('%b')

    def get_data_evento_hora(self):
        hs = self.data_evento - datetime.timedelta(hours=3)
        return hs.strftime("%H:%M")
