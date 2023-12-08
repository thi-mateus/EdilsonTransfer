from django import forms
from .models import Viagem


class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ['nome_usuario', 'email_usuario', 'telefone_usuario', 'origem', 'destino',
                  'data_ida', 'hora_ida', 'data_volta', 'hora_volta', 'ida_e_volta', 'passageiros', 'mensagem']

        widgets = {
            'nome_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome', 'name': 'name', 'required': 'required'}),
            'email_usuario': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'name': 'email'}),
            'telefone_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone', 'name': 'phone', 'required': 'required'}),
            'origem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Local', 'required': 'required'}),
            'destino': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Local', 'required': 'required'}),
            'passageiros': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade de passageiros'}),
            'data_ida': forms.DateInput(attrs={'class': 'form-control date-picker', 'placeholder': 'DD/MM/AAAA', 'required': 'required'}),
            'data_volta': forms.DateInput(attrs={'class': 'form-control date-picker', 'placeholder': 'DD/MM/AAAA'}),
            'hora_ida': forms.TimeInput(attrs={'class': 'form-control time-picker', 'placeholder': '00:00', 'required': 'required'}),
            'hora_volta': forms.TimeInput(attrs={'class': 'form-control time-picker', 'placeholder': '00:00'}),
            'ida_e_volta': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Escolha a opção'}),
            'mensagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a sua Mensagem', 'rows': '5',
                                               'name': 'msg'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Tornar campos obrigatórios
            self.fields['nome_usuario'].required = True
            self.fields['telefone_usuario'].required = True
            self.fields['origem'].required = True
            self.fields['destino'].required = True
            self.fields['data_ida'].required = True
            self.fields['hora_ida'].required = True
