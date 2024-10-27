from django.shortcuts import render
from .models import Fornecedor
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView)
from django.urls import reverse_lazy
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, "todos/index.html")


class FornecedorListView(ListView):
    model = Fornecedor
    template_name = "todos/fornecedor_list.html"
    
    def get_queryset(self):
        query = self.request.GET.get("q")  
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(
                Q(nome__icontains=query) |
                Q(cnpj__icontains=query) |
                Q(endereco__icontains=query) |
                Q(cidade__icontains=query) |
                Q(telefone__icontains=query)
            )
        return queryset

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
