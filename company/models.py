from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome/Razão')
    fantasy = models.CharField(max_length=100, verbose_name='Nome Fantasia')
    email = models.EmailField(unique=True, verbose_name='Email Corporativo')
    tel = models.CharField(max_length=11, blank=True, verbose_name='Telefone')
    cnae = models.CharField(max_length=7, verbose_name='CNAE-F')
    # Esse campo vai receber um Choice com as opções
    federal_regime = models.CharField(max_length=10, blank=True, verbose_name='Regime Federal')
    # Esse campo vai receber um Choice com as opções
    federal_state = models.CharField(max_length=10, blank=True, verbose_name='Regime Estadual')
    cnpj = models.CharField(max_length=14, unique=True, verbose_name='CNPJ')
    state_registration = models.CharField(max_length=15, unique=True, verbose_name='Inscrição Estadual')
    state_municipal = models.CharField(max_length=15, unique=True, verbose_name='Inscrição municipal')
    # O contador é um funcionario, esse campo vai receber um foreign key
    counter = models.CharField(max_length=100, verbose_name='Contador')
    # O contador é um funcionario, esse campo vai receber um foreign key
    administrator = models.CharField(max_length=100, verbose_name='Administrador')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
