from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import POST


class signup_form(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control my-2'}),
            'first_name':forms.TextInput(attrs={'class':'form-control my-2'}),
            'last_name':forms.TextInput(attrs={'class':'form-control my-2'}),
            'email':forms.EmailInput(attrs={'class':'form-control my-2'}),
        }







































# class post_form(forms.ModelForm):
#     class Meta:
#         model = POST
#         fields = ['user','title','post']
#         widgets = {
#             'user': forms.TextInput(attrs={'class': 'form-control my-2'}),
#             'title': forms.TextInput(attrs={'class': 'form-control my-2'}),
#             'post': forms.Textarea(attrs={'class': 'form-control my-2'}),
#
#         }
