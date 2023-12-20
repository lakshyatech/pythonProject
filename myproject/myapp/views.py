# myapp/views.py
from django.shortcuts import render
from .forms import MyForm


def form_page(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data (save to the database, send an email, etc.)
            # For now, you can print the form data to the console
            print(form.cleaned_data)
    else:
        form = MyForm()

    return render(request, 'form_page.html', {'form': form})
