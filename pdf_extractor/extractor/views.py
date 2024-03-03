from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UploadFileForm
from .utils import extract_data_from_pdf

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            result = extract_data_from_pdf(pdf_file)
            return render(request, 'extractor/result.html', {'result': result})
    else:
        form = UploadFileForm()
    return render(request, 'extractor/upload.html', {'form': form})
