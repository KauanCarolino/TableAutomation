from django.db import models

STATUS_PERSON = [
    (0, "Ativo"),
    (1, "Desativado"),
]

class Person(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=100)
    age = models.IntegerField(verbose_name="Idade")
    email = models.CharField(verbose_name="Email", max_length=255, unique=True)
    country = models.CharField(verbose_name="Estado", max_length=255)
    status = models.IntegerField(choices=STATUS_PERSON, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"