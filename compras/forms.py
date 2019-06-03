from django import  forms
from .models import Compra

class ComprarForm(forms.ModelForm):

    class Meta:
        model = Compra
        fields = ('data_compra', 'codigo_rastreio', 'metodo_envio',
                    'tempo_envio', 'produtos')

    