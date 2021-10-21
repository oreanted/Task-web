from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomRegisterForms
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForms(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ('New User Account created'))
            return redirect('list')
    else:
        register_form = CustomRegisterForms()
    return render(request, 'register.html', {'register_form': register_form})


