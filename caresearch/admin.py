from django.contrib import admin
from .models import CareProvider, CareProviderComments
from django_summernote.admin import SummernoteModelAdmin

@admin.register(CareProviderComments)
class CareProviderComments(SummernoteModelAdmin):

    summernote_fields = ('comment')

admin.site.register(CareProvider)
