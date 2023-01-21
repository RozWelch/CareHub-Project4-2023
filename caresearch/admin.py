from django.contrib import admin
from .models import CareProvider, CareProviderComments, CareSeeker
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

    list_display = ('business_name', 'main_contact_name', 'county', 'email', 'provider_approved_status')
    search_fields = ['business_name', 'main_contact_name', 'email', 'county',]
    list_filter = ('provider_approved_status', 'business_name')
    actions = ['approve_careprovider']

    def approve_careprovider(self, request, queryset):
        queryset.update(provider_approved_status=True)

@admin.register(CareSeeker)
class CareSeeker(SummernoteModelAdmin):

    list_display = ('first_name','second_name', 'email', 'county')
    search_fields = ['second_name','first_name', 'email', 'county']
    list_filter = ('second_name', 'careseeker_username' )
