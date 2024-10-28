from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Fornecedor, Produto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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
                Q(nome__icontains=query)
                | Q(cnpj__icontains=query)
                | Q(endereco__icontains=query)
                | Q(cidade__icontains=query)
                | Q(telefone__icontains=query)
            )
        return queryset


class FornecedorCreateView(CreateView):
    model = Fornecedor
    fields = "__all__"
    template_name = "todos/fornecedor_form.html"
    success_url = reverse_lazy("fornecedor_list")
    extra_context = {"titulo": "Cadastrar Fornecedor"}


class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    fields = "__all__"
    success_url = reverse_lazy("fornecedor_list")
    extra_context = {"titulo": "Atualizar Fornecedor"}


class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = "todos/fornecedor_confirm_delete.html"
    success_url = reverse_lazy("fornecedor_list")


class ProdutoCreateView(CreateView):
    model = Produto
    fields = "__all__"
    template_name = "todos/produtos_form.html"
    success_url = reverse_lazy("fornecedor_list")
    extra_context = {"titulo": "Cadastrar Produto"}


class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = "__all__"
    template_name = "todos/produtos_form.html"
    success_url = reverse_lazy("fornecedor_list")
    extra_context = {"titulo": "Atualizar Produto"}


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = "todos/produtos_confirm_delete.html"
    success_url = reverse_lazy("fornecedor_list")


class ProdutosPorFornecedorListView(ListView):
    model = Produto
    template_name = "todos/produtos_por_fornecedor.html"
    context_object_name = "produtos"

    def get_queryset(self):
        fornecedor_id = self.kwargs["fornecedor_id"]  # Pegue o ID do fornecedor da URL
        return Produto.objects.filter(fornecedor__id=fornecedor_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Inclua o fornecedor no contexto para mostrar seus detalhes na página
        context["fornecedor"] = get_object_or_404(
            Fornecedor, id=self.kwargs["fornecedor_id"]
        )
        return context
