from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import InvitationCode
from .forms import InvitationCodeForm

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def code_verify(request):
    session_key = f"user_ip_{get_client_ip(request)}"
    if request.method == 'POST':
        code = request.POST.get("code", "")
        code_obj = InvitationCode.objects.filter(code=code, expire__gt=timezone.now()).first()
        if code_obj:
            request.session[session_key] = True
            request.session.set_expiry(60)  # 60秒有效期
            messages.add_message(request, messages.SUCCESS, "验证成功")
        else:
            messages.add_message(request, messages.ERROR, "验证失败")
            if session_key in request.session:
                del request.session[session_key]

    return redirect('myapp:index')


def index(request):
    session_key = f"user_ip_{get_client_ip(request)}"
    # check if the user has passed the verification
    if session_key in request.session and request.session[session_key]:
        return render(request, 'myapp/index.html')
    else:
        print("我需要form!")
        form = InvitationCodeForm()
        return render(request, 'myapp/index.html', {'form': form,})