from django.shortcuts import render
from django.views import generic
from .models import CareProvider


class CareProviderList(generic.ListView):
    model = CareProvider
    queryset = CareProvider.objects.filter(status=1).order_by('business_name')
    template_name = 'careproviderslist.html'
    paginate_by = 6