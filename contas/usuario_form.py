from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import Perfil

class UserForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['password'].required = True
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'username': 'Username'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }



class PerfilForm(ModelForm):
    
    class Meta:
        model = Perfil
        fields = ['bio', 'foto']    
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            'foto':  forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }