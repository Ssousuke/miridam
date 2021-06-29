from django.db import models


class Address(models.Model):
    cep = models.CharField(max_length=8, verbose_name='CEP')
    address = models.CharField(max_length=100, verbose_name='Endereço')
    number = models.CharField(max_length=10, verbose_name='Número')
    district = models.CharField(max_length=25, verbose_name='Bairro')
    uf = models.CharField(max_length=2, verbose_name='UF')
    municipality = models.CharField(max_length=50, verbose_name='Municipio')
    nation = models.CharField(max_length=20, verbose_name='País')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
