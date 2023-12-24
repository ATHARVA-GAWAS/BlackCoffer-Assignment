from django.contrib import admin
from .models import Data
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class DataAdmin(ImportExportModelAdmin):
    list_display=[
            'end_year',
            'intensity',
            'sector',
            'topic',
            'insight',
            'url',
            'region',
            'start_year',
            'impact',
            'added',
            'published',
            'country',
            'relevance',
            'pestle',
            'source',
            'title',
            'likelihood',
    ]


admin.site.register(Data, DataAdmin)