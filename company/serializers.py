from rest_framework import serializers
from company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializers a Address object
    """

    class Meta:
        model = Company
        fields = (
            'name',
            'fantasy',
            'email',
            'tel',
            'cnae',
            'federal_regime',
            'federal_state',
            'cnpj',
            'state_registration',
            'state_municipal',
            'counter',
            'administrator',
        )
