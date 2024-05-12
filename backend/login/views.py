from django.shortcuts import render

from .models import CommonUser
from .forms import CommonUserForm


def index(request):

    form = CommonUserForm()
    return render(request, "login/index.html", {'form': form})  # noqa

