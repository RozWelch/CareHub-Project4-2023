from django.contrib import admin
from .models import CareProvider, CareProviderComments
from django_summernote.admin import SummernoteModelAdmin


@admin.register(CareProviderComments)
class CareProviderComments(SummernoteModelAdmin):

    list_display = ('careprovider', 'name', 'approved', 'date_created')
    search_fields = ['careprovider', 'comment']
    summernote_fields = ('comment')
    list_filter = ('approved', 'date_created')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(CareProvider)
class CareProvider(SummernoteModelAdmin):

    list_display = (
       'careprovider_username', 'business_name', 'type_of_care',
       'main_contact_name', 'county', 'email', 'description',
       'provider_approved_status'
        )
    search_fields = [
        'business_name', 'type_of_care',
        'main_contact_name', 'email', 'county',
        ]
    list_filter = ('provider_approved_status', 'type_of_care', 'business_name')
    actions = ['approve_careprovider']

    def approve_careprovider(self, request, queryset):
        queryset.update(provider_approved_status=True)
