from django import forms


class BookingForm(forms.Form):
    local_embarque = forms.CharField(
        label='Local de Embarque',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o Local'})
    )
    local_desembarque = forms.CharField(
        label='Local de Desembarque',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o Local'}),
    )
    passageiros = forms.IntegerField(
        label='Passageiros',
        initial=1,
        widget=forms.TextInput(attrs={'placeholder': 'Passageiros'}),
    )
    tipo_veiculo = forms.ChoiceField(
        label='Capacidade do veículo',
        choices=[(1, 'Indiferente'),
                 (2, '4 passageiros'), (3, '6 passageiros')],
        widget=forms.TextInput(attrs={'placeholder': 'Escolha o Táxi'}),
    )
    data_embarque = forms.DateField(
        label='Data de Embarque',
        widget=forms.TextInput(
            attrs={'class': 'form-control date-picker', 'placeholder': 'DD/MM/AAAA'})
    )
    hora_embarque = forms.TimeField(
        label='Hora de Embarque',
        widget=forms.TextInput(
            attrs={'class': 'form-control time-picker', 'placeholder': '00:00 AM'})
    )
    idade_motorista = forms.ChoiceField(
        label='Ida e Volta',
        choices=[(1, 'Somente Ida'),
                 (2, 'Ida e Volta')],
        widget=forms.TextInput(attrs={'placeholder': 'Escolha a opção'}),
    )
