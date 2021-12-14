from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.files.storage import default_storage




from .parser import proccesing_uploaded_file
from .forms import UploadFileForm
# Create your views here.



def index(request):
    return render(request, 'exch/index.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_name = default_storage.save(file.name, file)
            proccesing_uploaded_file(file_name)
            return HttpResponse(f'Загружен {file_name}')
        
    else:
        form = UploadFileForm()
    return render(request, 'exch/upload.html', {'form': form})

import xml.etree.ElementTree as ET





def proccesing_uploaded_file(xmlfile):
    tree = ET.parse(xmlfile)
    root_xml = tree.getroot()
    for child in root_xml.iter('name'):
        print(child.text)
