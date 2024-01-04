from django.urls import path
from .views import home, BankAccountListView, BankAccountCreateView, BankAccountUpdateView, BankAccountDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('manage_accounts/', BankAccountListView.as_view(), name='manage_accounts'),
    path('create_account/', BankAccountCreateView.as_view(), name='create_account'),
    path('edit_account/<int:pk>/', BankAccountUpdateView.as_view(), name='edit_account'),
    path('delete_account/<int:pk>/', BankAccountDeleteView.as_view(), name='delete_account'),
]
