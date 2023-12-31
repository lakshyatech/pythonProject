from django.urls import path
from .views import home, create_account, manage_accounts, edit_account, delete_account

urlpatterns = [
    path('', home, name='home'),
    path('create_account/', create_account, name='create_account'),
    path('manage_accounts/', manage_accounts, name='manage_accounts'),
    path('edit_account/<int:account_id>/', edit_account, name='edit_account'),
    path('delete_account/<int:account_id>/', delete_account, name='delete_account'),
]
