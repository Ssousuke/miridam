from django.db import models


class Department(models.Model):
    department = models.CharField(max_length=50, verbose_name='Departamento')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Atualização')

    def __str__(self):
        return self.department

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


class Occupation(models.Model):
    occupation = models.CharField(max_length=50, verbose_name='Cargo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, verbose_name='Departamento')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Atualização')

    def __str__(self):
        return self.occupation

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
