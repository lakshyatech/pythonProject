from django.shortcuts import render
from django.http import HttpResponse
from .models import RegisterModel
from .form import RegisterForm
from django.views import View

# class HomeView(View):
#     def get(self,request):
#         form= RegisterForm()
#         return render(request,'index.html',{'form':form})
#     def post(self, request):
#         form=RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request,'index.html',{'form':form})
#
def get(request):
    return render(request,"index.html")
def post(request):
    print("Mahendra")
    s=['Python','Java','javascript','C++']
    if request.method == "POST":
        User_name=request.POST['Username']
        Email=request.POST['Email']
        password=request.POST['pssword']
        gender=request.POST['gender']
        city=request.POST['countries']
        skill = request.POST.getlist('skill')

        print(skill)
        if skill==['Python']:
            print('Python')
        if skill==['Java']:
            print('Java')
        if skill==['javascript']:
            print('javascript')
        if skill==['C++']:
            print('C++')
        if skill==[]:
            print("Nothing")

        form_field=RegisterModel(
            User_name=User_name,
            Email=Email,
            password=password,
            gender=gender,
            city=city,
            skill=skill

    )
        form_field.save()
    return render(request,'Contact.html')
