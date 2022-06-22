from django import forms

from oficina.models import *


class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['cliente', 'carro', 'mecanico', 'descricao', 'valor']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'telefone', 'endereco', 'cidade']

