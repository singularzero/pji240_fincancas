from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from financas.models import Categoria, Gastos, Receitas
from financas.serializers import CategoriaSerializer, GastoSerializer, ReceitaSerializer

# Create your views here.
@csrf_exempt
def categoriaApi(request, id=None):
    if request.method == 'GET':
        try:
            if id is not None:
                # Retorna a categoria com o ID fornecido
                categoria = Categoria.objects.get(id=id)
                return JsonResponse({'id': categoria.id, 'nome': categoria.nome})
            else:
                # Retorna todas as categorias
                categorias = Categoria.objects.all()
                categorias_serializer = CategoriaSerializer(categorias, many=True)
                return JsonResponse(categorias_serializer.data, safe=False)
                # categorias_serializer = list(Categoria.objects.values())
                return JsonResponse(categorias, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Categoria não encontrada."}, status=404)
    elif request.method == 'POST':
        categoria_data = JSONParser().parse(request)
        categoria_serializer = CategoriaSerializer(data=categoria_data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return JsonResponse({"message":"CADASTRO DE CATEGORIA REALIZADO COM SUCESSO"}, status=201)
        return JsonResponse(categoria_serializer.errors, status=400)

    elif request.method == 'PUT':
        categoria_data = JSONParser().parse(request)
        try:            
            categoria = Categoria.objects.get(id=categoria_data.get('id'))
            categoria_serializer = CategoriaSerializer(categoria,data=categoria_data)
            if categoria_serializer.is_valid():
                categoria_serializer.save()
                return JsonResponse({"message": "Cadastro de categoria atualizado com sucesso."}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Categoria não encontrada para atualização."}, status=404)
    
    elif request.method == 'DELETE':
        try:
            categoria = Categoria.objects.get(id=id)
            categoria.delete()
            return JsonResponse({"message": "Categoria deletada com sucesso."}, status=204)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Categoria não encontrada para exclusão."}, status=404)               
        except Exception as e:
            return JsonResponse({"error": f"Erro interno do servidor: {str(e)}"}, status=500)          
    else:
        return JsonResponse({"error": "Método não permitido."}, status=405)
    


"""
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

"""