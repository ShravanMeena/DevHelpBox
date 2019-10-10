from django import forms
from .models import *

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome', 'sobrenome', 'nickname', 'data_nascimento', 'email', 'pessoa_genero_sexual_idpessoa_genero_sexual')

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ('nome', 'data_inicio', 'horario_inicio', 'horario_fim', 'local', 'evento_tipo_idevento_tipo')

'''
class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('nome', 'datanasc', 'email')
        widgets = {
            'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'datanasc': forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
            'email': forms.EmailInput(),
        }
        labels = {
            'nome': ('Nome Completo:'),
            'datanasc': ('Data de Nascimento'),
        }
        help_texts = {
            'nome': ('Teu nome, anta'),
            'datanasc': ('esqueceu?'),
            'email': ('email@provedor.com'),
        }
        error_messages = {
            'name': {
                'max_length': ('Oh a avacalhacao mah'),
            }
        }
'''
