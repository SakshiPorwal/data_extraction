from django.db import models

class UploadedPDF(models.Model):
    pdf_file = models.FileField(upload_to='pdf_files/')
    extracted_data = models.TextField(blank=True)
