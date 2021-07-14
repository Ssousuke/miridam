from django.shortcuts import render
from django.views.generic import ListView
from address.models import Address


class AddressListView(ListView):
    model = Address
    template_name = 'address_index.html'
