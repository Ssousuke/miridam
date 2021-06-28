from django.db import models


class Address(models.Model):
    cep = models.CharField()
    address = models.CharField()
    number = models.CharField()
    district = models.CharField()
    uf = models.CharField()
    municipality = models.CharField()
    nation = models.CharField()

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
