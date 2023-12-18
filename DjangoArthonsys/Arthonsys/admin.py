from django.contrib import admin
from .models import RegisterModel

@admin.register(RegisterModel)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ['User_name','Email','password','gender','city','skill']