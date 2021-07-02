from rest_framework import serializers
from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializes a Employee model
    """

    class Meta:
        model = Employee
        fields = (
            'profile_image',
            'name',
            'surname',
            'birth_date',
            'father',
            'mother',
            'ethnicity',
            'scholarity',
            'gender',
            'rg',
            'identity_issue_date',
            'cpf',
            'ctps',
            'serie_ctps',
            'ctps_issue_date',
            'salary',
            'admission_date',
            'department',
            'occupation',
        )
