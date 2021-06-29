from django.db import models

ETHNIC_COMPOSITION_CHOICES = [
    ('Branca', 'Branca'),
    ('Preta', 'Preta'),
    ('Amarela', 'Amarela'),
    ('Parda', 'Parda'),
    ('Indígena', 'Indígena'),
    ('Sem Declaração', 'Sem Declaração'),
]
EDUCATION_LEVEL_CHOICES = [
    ('01', 'Analfabeto'),
    ('02', 'Até 4ª série incompleta do 1º grau (ensino fundamental)'),
    ('03', '4ª série completa do 1º grau (ensino fundamental)'),
    ('04', '5ª a 8ª série incompleta do 1º grau (ensino fundamental)'),
    ('05', '1º grau completo (ensino fundamental)'),
    ('06', 'Sem 	2º grau incompleto (ensino médio)'),
    ('07', '	2º grau completo (ensino médio)'),
    ('08', 'Superior Incompleto'),
    ('09', 'Superior Completo'),
    ('10', 'Pós-Graduação/Especialização'),
    ('11', 'Mestrado'),
    ('12', 'Doutorado'),
    ('13', 'Pós-Doutorado'),
]
GENDER_CHOICES = [
    ('M', 'M'),
    ('F', 'F'),
]


class Employee(models.Model):
    profile_image = models.ImageField(upload_to='func_perfil_image', verbose_name='Imagem de Identificação')
    name = models.CharField(max_length=100, verbose_name='Nome Completo')
    surname = models.CharField(max_length=15, blank=True, verbose_name='Apelido/Nome Social')
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    father = models.CharField(max_length=100, verbose_name='Pai')
    mother = models.CharField(max_length=100, verbose_name='Mãe')
    ethnicity = models.CharField(max_length=15, choices=ETHNIC_COMPOSITION_CHOICES, verbose_name='Composição étnica')
    scholarity = models.CharField(max_length=2, choices=EDUCATION_LEVEL_CHOICES, verbose_name='Escolaridade')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Sexo')
    rg = models.CharField(max_length=12, unique=True, verbose_name='RG')
    identity_issue_date = models.DateField(verbose_name='Data de Emissão "RG"')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    ctps = models.CharField(max_length=8, unique=True, verbose_name='CTPS')
    serie_ctps = models.CharField(max_length=5, unique=True, verbose_name='Série CTPS')
    ctps_issue_date = models.DateField(verbose_name='Data de Emissão CTPS')
    salary = models.FloatField(verbose_name='Salário')
    admission_date = models.DateField(verbose_name='Data de Admissão')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
