from rest_framework import serializers
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    """
    Serializers a Address object
    """

    class Meta:
        model = Address
        fields = (
            'cep',
            'address',
            'number',
            'district',
            'uf',
            'municipality',
            'nation',
        )
