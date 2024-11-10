import plotly.express as px
import plotly.graph_objs as go
from django.shortcuts import render
from .models import Categoria, Gastos, Receitas 


def grafico_view(request):
    # Obtendo os dados de Gastos, Receitas e Categorias
    categorias = Categoria.objects.all()
    gastos = Gastos.objects.all()
    receitas = Receitas.objects.all()

    # Criando um dicionário para armazenar os valores de gastos por categoria
    categorias_gastos = {}
    for gasto in gastos:
        categoria_nome = gasto.categoria.nome
        if categoria_nome not in categorias_gastos:
            categorias_gastos[categoria_nome] = 0
        categorias_gastos[categoria_nome] += float(gasto.valor)

     # Criando um dicionário para armazenar os valores de receitas por categoria
    categorias_receitas = {}
    for receita in receitas:
        categoria_nome = receita.categoria.nome
        if categoria_nome not in categorias_receitas:
            categorias_receitas[categoria_nome] = 0
        categorias_receitas[categoria_nome] += float(receita.valor)
    
    # --- Gráfico de Pizza de Gastos por Categoria ---
    fig_pizza_gastos = px.pie(
        names=list(categorias_gastos.keys()), 
        values=list(categorias_gastos.values()),
        title="Distribuição de Gastos por Categoria"
    )

     # --- Gráfico de Pizza de Receitas por Categoria ---
    fig_pizza_receitas = px.pie(
        names=list(categorias_receitas.keys()), 
        values=list(categorias_receitas.values()),
        title="Distribuição de Receitas por Categoria"
    )

    # --- Gráfico de Barra de Gastos por Categoria ---
    fig_bar_gastos = go.Figure(go.Bar(
        x=list(categorias_gastos.keys()),
        y=list(categorias_gastos.values()),
        name="Gastos por Categoria"
    ))
    fig_bar_gastos.update_layout(title="Gastos por Categoria")

    # --- Gráfico de Barra de Receitas por Categoria ---
    fig_bar_receitas = go.Figure(go.Bar(
        x=list(categorias_receitas.keys()),
        y=list(categorias_receitas.values()),
        name="Receitas por Categoria"
    ))
    fig_bar_receitas.update_layout(title="Receitas por Categoria")

    # Convertendo os gráficos para HTML para inseri-los no template
    context = {
        'fig_pizza_gastos': fig_pizza_gastos.to_html(full_html=False),
        'fig_pizza_receitas': fig_pizza_receitas.to_html(full_html=False),
        'fig_bar_gastos': fig_bar_gastos.to_html(full_html=False),
        'fig_bar_receitas': fig_bar_receitas.to_html(full_html=False),
    }

    return render(request, 'financas/grafico.html', context)


""""
    # Obtendo os dados de Gastos e Receitas
    categorias = Categoria.objects.all()
    gastos = Gastos.objects.all()
    receitas = Receitas.objects.all()

    
    

    def graficos_financeiros(request):
    # Dados simulados - substitua pelos dados reais do banco de dados
    categorias = ['Alimentação', 'Transporte', 'Lazer', 'Educação']
    valores_gastos = [500, 300, 200, 400]
    valores_receitas = [700, 500, 300, 200]

     # --- Gráfico de Pizza de Gastos por Categoria ---
    categorias_gastos = {}
    for gasto in gastos:
        if gasto.categoria.nome not in categorias_gastos:
            categorias_gastos[gasto.categoria.nome] = 0
        categorias_gastos[gasto.categoria.nome] += float(gasto.valor)
    
    fig_pizza = px.pie(
        names=list(categorias_gastos.keys()), 
        values=list(categorias_gastos.values()),
        title="Distribuição de Gastos por Categoria"
    )

    # --- Gráfico de Barra de Receitas por Categoria ---
    categorias_receitas = {}
    for receita in receitas:
        if receita.categoria.nome not in categorias_receitas:
            categorias_receitas[receita.categoria.nome] = 0
        categorias_receitas[receita.categoria.nome] += float(receita.valor)

    fig_bar = px.bar(
        x=list(categorias_receitas.keys()), 
        y=list(categorias_receitas.values()),
        labels={'x': 'Categoria', 'y': 'Valor'},
        title="Receitas por Categoria"
    )
"""
    