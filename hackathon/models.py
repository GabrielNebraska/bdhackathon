from django.core.exceptions import ValidationError
from django.db import models 


def only_numbers(value): 
    if value.isdigit()==False:
        raise ValidationError('Este campo deve conter apenas números')



# Create your models here.
class Cargo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class usuario(models.Model):

    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    endereco = models.CharField(max_length=350, null=False )
    email = models.EmailField(null=False, blank=False)
    senha = models.CharField(max_length=20, null=False, blank=False)
    telefone = models.CharField(validators=[only_numbers], max_length=11)
    cargo = models.ForeignKey(
        Cargo, on_delete=models.PROTECT, related_name="funcionarios"
    )

    def __str__(self):
        return f"{self.nome} ({self.matricula})"