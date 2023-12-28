from django.urls import path
from .views import home,create_account

urlpatterns = [
    path('', home, name='home'),
    path('create_account/', create_account, name='create_account'),
]
