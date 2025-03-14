from django.forms import ModelForm
from django import forms
from .models import Contato


class ContatoForm(ModelForm):

    class Meta:
        model = Contato
        fields = '__all__'
        widgets = {
            'assunto': forms.Select(attrs={'class': 'form-select mb-3'}),
            'nome': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }