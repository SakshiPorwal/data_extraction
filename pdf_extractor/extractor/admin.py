from django.contrib import admin
from .models import UploadedPDF

@admin.register(UploadedPDF)
class UploadedPDFAdmin(admin.ModelAdmin):
    list_display = ('pdf_file', 'extracted_data',)
    search_fields = ('pdf_file',)
