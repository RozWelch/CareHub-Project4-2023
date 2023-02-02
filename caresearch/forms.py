from .models import CareProviderComments
from django import forms


class CareProviderCommentsForm(forms.ModelForm):
    class Meta:
        model = CareProviderComments
        fields = ('comment',)


class ProviderForm(forms.ModelForm):
    class Meta:
        model = CareProvider
        fields = [
            'business_name',
            'type_of_care',
            'main_contact_name', 'address_line_1',
            'county', 'phone_number', 'email',
            'disabled_parking', 'provider_image',
            ]


class ProviderForm(forms.ModelForm):
    class Meta:
        model = CareProvider
        fields = [
            'careprovider_username',
            'type_of_care',
            'main_contact_name', 'address_line_1',
            'county', 'phone_number', 'email',
            'disabled_parking', 'provider_image',
            ]
