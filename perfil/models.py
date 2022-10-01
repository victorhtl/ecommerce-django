from django.db import models
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,
                                   verbose_name='Usuário')
    idade = models.PositiveIntegerField(default=0)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=40)
    numero = models.CharField(max_length=8)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=40)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=40)
    estado = models.CharField(
        max_length=2,
        default='PR',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        ))  

    # Nome que aparece na área administrativa
    def __str__(self):
        return self.user

    # Ajeitando o nome que aparece na área administrativa
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
