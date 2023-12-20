# myapp/forms.py
from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)
    subscribe_newsletter = forms.BooleanField(label='Subscribe to Newsletter', required=False)
    gender = forms.ChoiceField(label='Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
                               widget=forms.RadioSelect)
