from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ["email", "username", "password"]

    def clean_password(self):
        raw_password = self.cleaned_data['password']
        print(raw_password)
        validate_password(raw_password)
        return raw_password
