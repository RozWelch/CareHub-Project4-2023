from .models import CareProviderComments, CareProvider
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
            'business_name',
            'type_of_care',
            'main_contact_name', 'address_line_1',
            'county', 'phone_number', 'email',
            'description',
            'disabled_parking', 'provider_image',
            ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = CareProvider
        fields = [
            'business_name',
            'type_of_care',
            'main_contact_name', 'address_line_1',
            'county', 'phone_number', 'email',
            'disabled_parking', 'provider_image',
            ]
