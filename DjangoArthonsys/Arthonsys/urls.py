from django.urls import path
from . import views

urlpatterns = [
    path('', views.get,),
    path('Contacts/', views.post, name="Contacts"),
    # path('',views.Home.as_view())
    # path('Contacts/')
]
