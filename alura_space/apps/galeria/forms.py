from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels = {
            'descricao':'Descrição',
            'data':'Data de registro',
            'usuario':'Usuário',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control','placeholder':'Digite um nome para o Post'}),
            'legenda': forms.TextInput(attrs={'class':'form-control','placeholder':'Adicione uma legenda para o Post...'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control','placeholder':'Digite uma descrição para o Post'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),

        }