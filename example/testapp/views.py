from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib.auth.models import User

from testapp import forms

def account_register(request):
    form = forms.UserForm()
    if request.method == "POST":
        username = request.POST.get("username")
        if username is not None:
            try:
                instance = User.objects.get(username__iexact=username)
            except User.DoesNotExist:
                form = forms.UserForm(request.POST)
                if form.is_valid():
                    form.save()
                    return render(request, "success.html", {})

    return render(request, "register.html", {'form': form})

