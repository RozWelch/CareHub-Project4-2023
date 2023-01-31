from .models import CareProviderComments, CareProvider
from django import forms


class CareProviderCommentsForm(forms.ModelForm):
    class Meta:
        model = CareProviderComments
        fields = ('comment',)


class ProviderForm(forms.ModelForm):
    class Meta:
        model = CareProvider
        fields = ('business_name',)