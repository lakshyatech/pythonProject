from django.db import models
from django.contrib.auth.models import AbstractUser
class RegisterModel(models.Model):
    city_c=(
        ('Jaipur','Jaipur'),
        ('Jodhpur', 'Jodhpur'),
        ('Kota', 'Kota'),
    )
    skill_c = (
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('javascript', 'javascript'),
        ('C++','C++'),
    )
    User_name=models.CharField(max_length=100)
    Email=models.EmailField()
    password=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    city=models.CharField(choices=city_c, max_length=100)
    skill=models.CharField(choices=skill_c,max_length=100)


    # Gander_choices = [('M','male'),('F', 'Female'), ]
    # opetion1='opetion1'
    # opetion2='opetion2'
    # opetion3='opetion3'
    # CHOICES = [
    #     (opetion1, 'Option One'),
    #     (opetion2, 'Option Two'),
    #     (opetion3, 'Option Three'),
    # ]
    #
    # Skills_CHOICES = [('C', 'Python'),('sf', 'Java'),('la', 'Javascript'),]
    # User_Name=models.CharField(max_length=100)
    # User_Email=models.EmailField(max_length=200)
    # password=models.CharField(max_length=200)
    # Gander=models.CharField(max_length=1,choices=Gander_choices,default='0')
    # Skills = models.CharField(max_length=2,choices=Skills_CHOICES,default='C',verbose_name='Skills')
    # selected_options = models.ManyToManyField(
    #     'self',  # Assuming you want to allow selecting options from this model
    #     blank=True,
    #     symmetrical=False,
    #     related_name='related_selected_options',
    #     verbose_name='Selected Options',
    #     # widget=models.CheckboxSelectMultiple,
    #     choices=CHOICES,
    # )
    # def __str__(self) -> str:
    #     return self.User_Name
