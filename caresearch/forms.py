from .models import CareProviderComments
from django import forms


class CareProviderCommentsForm(forms.ModelForm):
    class Meta:
        model = CareProviderComments
        fields = ('comment',)
