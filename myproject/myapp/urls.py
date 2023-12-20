# myapp/urls.py
from django.urls import path
from .views import form_page

urlpatterns = [
    path('', form_page, name='form_page'),
]
