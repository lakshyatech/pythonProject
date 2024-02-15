# datatableapp/urls.py
from django.urls import path
from .views import DataTableView

app_name = 'datatableapp'

urlpatterns = [
    path('datatable/', DataTableView.as_view(), name='datatable'),
]
