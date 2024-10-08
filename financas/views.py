# from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria, Gastos, Receitas


# Create your views here.


class CategoriaListView(ListView):
    model = Categoria


class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ["nome"]
    success_url = reverse_lazy("categoria_list")


class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ["nome"]
    success_url = reverse_lazy("categoria_list")


class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy("categoria_list")


class GastosListView(ListView):
    model = Gastos


class GastosCreateView(CreateView):
    model = Gastos
    fields = ["categoria", "retirado_em", "valor"]
    success_url = reverse_lazy("gastos_list")


class GastosUpdateView(UpdateView):
    model = Gastos
    fields = ["categoria", "retirado_em", "valor"]
    success_url = reverse_lazy("gastos_list")


class GastosDeleteView(DeleteView):
    model = Gastos
    success_url = reverse_lazy("gastos_list")


class ReceitasListView(ListView):
    model = Receitas


class ReceitasCreateView(CreateView):
    model = Receitas
    fields = ["categoria", "adicionado_em", "valor"]
    success_url = reverse_lazy("receitas_list")


class ReceitasUpdateView(UpdateView):
    model = Receitas
    fields = ["categoria", "adicionado_em", "valor"]
    success_url = reverse_lazy("receitas_list")


class ReceitasDeleteView(DeleteView):
    model = Receitas
    success_url = reverse_lazy("receitas_list")
