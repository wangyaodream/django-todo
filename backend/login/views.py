from django.shortcuts import render

from .models import CommonUser
from .forms import LoginUserForm, RegisterUserForm


def index(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            user = CommonUser.objects.get(name=name, password=password)
            if user:
                return render(request, "login/profile.html", {'user': user})
    else:
        form = LoginUserForm()
        return render(request, "login/index.html", {'form': form})  # noqa


def register(request):
    # if request.method == "POST":
    #     form = RegisterUserForm() 
    #     if form.is_valid():
    #         form.save()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "login/index.html")
    else:
        form = RegisterUserForm()
        return render(request, "login/register.html", {'form': form})  # noqa
