from django.forms import ModelForm
from address.models import Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
