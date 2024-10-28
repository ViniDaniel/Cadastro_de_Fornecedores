"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from todos.views import (
    index,
    FornecedorListView,
    FornecedorCreateView,
    FornecedorUpdateView,
    FornecedorDeleteView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView,
    ProdutosPorFornecedorListView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("fornecedores", FornecedorListView.as_view(), name="fornecedor_list"),
    path("create", FornecedorCreateView.as_view(), name="fornecedor_form"),
    path(
        "atualizar/<int:pk>/", FornecedorUpdateView.as_view(), name="fornecedor_update"
    ),
    path("deletar/<int:pk>/", FornecedorDeleteView.as_view(), name="fornecedor_delete"),
    path("produtos", ProdutoCreateView.as_view(), name="produtos_form"),
    path(
        "produtos/atualizar/<int:pk>/",
        ProdutoUpdateView.as_view(),
        name="produtos_update",
    ),
    path(
        "produtos/deletar/<int:pk>/",
        ProdutoDeleteView.as_view(),
        name="produtos_delete",
    ),
    path(
        "fornecedores/<int:fornecedor_id>/produtos/",
        ProdutosPorFornecedorListView.as_view(),
        name="produtos_por_fornecedor",
    ),
]
