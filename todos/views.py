from django.shortcuts import render
from .models import Fornecedor
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView)
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, "todos/index.html")


class FornecedorListView(ListView):
    model = Fornecedor
    template_name = "todos/fornecedor_list.html"


class FornecedorCreateView(CreateView):
    model = Fornecedor
    fields = "__all__"
    template_name = "todos/fornecedor_form.html"
    success_url = reverse_lazy("index")
    extra_context = {'titulo': 'Cadastrar Fornecedor'}



class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    fields = "__all__"
    success_url = reverse_lazy("fornecedor_list")
    extra_context = {'titulo': 'Atualizar Fornecedor'}



class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = "todos/fornecedor_confirm_delete.html"
    success_url = reverse_lazy("fornecedor_list")
