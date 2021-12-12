from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage




from .forms import UploadFileForm
# Create your views here.



def index(request):
    return render(request, 'exch/index.html')


def upload_file(request):
    form = UploadFileForm()
    return render(request, 'exch/upload.html', {'form': form})

""" def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            proccesing_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'exch/upload.html', {'form': form}) """


def proccesing_uploaded_file():
    pass