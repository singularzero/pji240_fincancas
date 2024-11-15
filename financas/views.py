from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Gastos, Receitas, Bitcoin
import plotly.express as px
from plotly.offline import plot
import plotly.io as pio
from .models import Gastos, Receitas, Categoria
from django.urls import reverse_lazy

def grafico_view(request):
    # Obter dados para o gráfico de pizza de gastos
    gastos_data = Gastos.objects.values('categoria').annotate(total=Sum('valor'))
    labels_gastos = [item['categoria'] for item in gastos_data]
    valores_gastos = [float(item['total']) for item in gastos_data]
    fig_gastos_pizza = px.pie(values=valores_gastos, names=labels_gastos, title="Distribuição de Gastos")

    # Obter dados para o gráfico de pizza de receitas
    receitas_data = Receitas.objects.values('categoria').annotate(total=Sum('valor'))
    labels_receitas = [item['categoria'] for item in receitas_data]
    valores_receitas = [float(item['total']) for item in receitas_data]
    fig_receitas_pizza = px.pie(values=valores_receitas, names=labels_receitas, title="Distribuição de Receitas")

    # Obter dados para o gráfico de barras de gastos
    fig_gastos_bar = px.bar(x=labels_gastos, y=valores_gastos, title="Gastos por Categoria", labels={'x': 'Categoria', 'y': 'Total Gasto'})
    
    # Obter dados para o gráfico de barras de receitas
    fig_receitas_bar = px.bar(x=labels_receitas, y=valores_receitas, title="Receitas por Categoria", labels={'x': 'Categoria', 'y': 'Total Receita'})

    # Converter os gráficos para HTML
    grafico_gastos_pizza_html = pio.to_html(fig_gastos_pizza, full_html=False)
    grafico_receitas_pizza_html = pio.to_html(fig_receitas_pizza, full_html=False)
    grafico_gastos_bar_html = pio.to_html(fig_gastos_bar, full_html=False)
    grafico_receitas_bar_html = pio.to_html(fig_receitas_bar, full_html=False)

    # Passar os gráficos para o contexto do template
    context = {
        'grafico_gastos_pizza': grafico_gastos_pizza_html,
        'grafico_receitas_pizza': grafico_receitas_pizza_html,
        'grafico_gastos_bar': grafico_gastos_bar_html,
        'grafico_receitas_bar': grafico_receitas_bar_html,
    }

    return render(request, "financas/grafico.html", context)


def index_view(request):
    return render(request, "financas/index.html")


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

class BitcoinListView(ListView):
    model = Bitcoin


class BitcoinCreateView(CreateView):
    model = Bitcoin
    fields = ["adicionado_em", "valor"]
    success_url = reverse_lazy("bitcoin_list")


class BitcoinUpdateView(UpdateView):
    model = Bitcoin
    fields = ["adicionado_em", "valor"]
    success_url = reverse_lazy("bitcoin_list")


class BitcoinDeleteView(DeleteView):
    model = Bitcoin
    success_url = reverse_lazy("bitcoin_list")
