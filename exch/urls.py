from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('uploadf/', upload_file, name='upload_file')
]