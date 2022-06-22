from django.shortcuts import render, redirect

from oficina.forms import OrcamentoForm, ClienteForm
from oficina.models import Orcamento


# Create your views here.

def list_orcamento(request):
    orcamento = Orcamento.objects.all()
    return render(request, 'orcamento.html', {'orcamento': orcamento})


def create_orcamento(request):
    form = OrcamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_orcamento')

    return render(request, 'orcamento-form.html', {'form': form})


def update_orcamento(request, id):
    orcamento = Orcamento.objects.get(id=id)
    form = OrcamentoForm(request.POST or None, instance=orcamento)

    if form.is_valid():
        form.save()
        return redirect('list_orcamento')

    return render(request, 'orcamento-form.html', {'form': form, 'orcamento': orcamento})


def delete_orcamento(request, id):
    orcamento = Orcamento.objects.get(id=id)

    if request.method == 'POST':
        orcamento.delete()
        return redirect('list_orcamento')

    return render(request, 'orcamento-delete-confirm.html', {'orcamento': orcamento})

#==================================================================


def create_cliente(request):
    form = ClienteForm(request.POST or None)
    print("ola")
    if form.is_valid():
        form.save()
        return redirect('list_orcamento')

    return render(request, 'cliente-form.html', {'form': form})