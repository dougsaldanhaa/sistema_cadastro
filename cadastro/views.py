from django.shortcuts import render, redirect

from cadastro.models import Pessoa
from .forms import PessoaForm

def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'cadastro/cadastrar_pessoa.html', {'form': form})

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'cadastro/lista_pessoas.html', {'pessoas': pessoas})
