from  django import  forms
from  .models import RegisterModel

Geder_choice=[
    ('Male','Male'),
    ('Female','Female')
]
skill_choice=[
    ('Python','Python'),
    ('Java', 'Java'),
    ('JavaScript', 'JavaScript'),
    ('C++', 'C++'),

]
city_choice=[
    ('Jaipur','Jaipur'),
    ('Jodhpur', 'Jodhpur'),
    ('Kota', 'Kota'),
]
class RegisterForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=Geder_choice,widget=forms.RadioSelect)
    skill=forms.MultipleChoiceField(choices=skill_choice)
    city=forms.ChoiceField(choices=city_choice,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model= RegisterModel
        fields=['User_name','Email','password','gender','city','skill']






# from django.core import validators
# class RegisterForm(forms.Form):
#     Gander_choices=[
#         ('M','male'),
#         ('F', 'Female'),
#
#     ]
#     user_name=forms.CharField()
#     user_email=forms.EmailField()
#     password=forms.CharField(widget=forms.PasswordInput)
#     Gander=forms.ChoiceField(choices=Gander_choices,widget=forms.Select(attrs={'class':'form-control'}))


