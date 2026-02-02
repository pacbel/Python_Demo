from django.db import models

# Create your models here.

class Contact(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self) -> str:
        return f'{self.nome} ({self.telefone})'
