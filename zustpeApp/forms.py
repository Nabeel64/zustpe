
from django import forms
from django.forms.fields import Field
from .models import User
from django.contrib.auth.forms import UserCreationForm

class Signup(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter Password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Confirm Password"
    }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','userpic']
        labels = {'userpic': 'proflie pic'}
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
            }),
            "first_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Firstname",
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Lastname",
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Email",
            }),
        }