from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from financas.views import grafico_view
from financas import views
from django.contrib import admin
from django.urls import path, include


from financas.views import (    
    ReceitasListView,
    ReceitasCreateView,
    ReceitasUpdateView,
    ReceitasDeleteView,
    GastosListView,
    GastosCreateView,
    GastosUpdateView,
    GastosDeleteView,
    CategoriaListView,
    CategoriaCreateView,
    CategoriaUpdateView,
    CategoriaDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("grafico/", views.grafico_view, name="grafico"),  
    path(
        "categoria/",
        CategoriaListView.as_view(),
        name="categoria_list",
    ),
    path("index/", views.index_view, name="index"),
    path(
        "categoria/create/",
        CategoriaCreateView.as_view(),
        name="categoria_create",
    ),
    path(
        "categoria/update/<int:pk>/",
        CategoriaUpdateView.as_view(),
        name="categoria_update",
    ),
    path(
        "categoria/delete/<int:pk>/",
        CategoriaDeleteView.as_view(),
        name="categoria_delete",
    ),
    path(
        "gastos/",
        GastosListView.as_view(),
        name="gastos_list",
    ),
    path(
        "gastos/create/",
        GastosCreateView.as_view(),
        name="gastos_create",
    ),
    path(
        "gastos/update/<int:pk>/",
        GastosUpdateView.as_view(),
        name="gastos_update",
    ),
    path(
        "gastos/delete/<int:pk>/",
        GastosDeleteView.as_view(),
        name="gastos_delete",
    ),
    path(
        "receitas/",
        ReceitasListView.as_view(),
        name="receitas_list",
    ),
    path(
        "receitas/create/",
        ReceitasCreateView.as_view(),
        name="receitas_create",
    ),
    path(
        "receitas/update/<int:pk>/",
        ReceitasUpdateView.as_view(),
        name="receitas_update",
    ),
    path(
        "receitas/delete/<int:pk>/",
        ReceitasDeleteView.as_view(),
        name="receitas_delete",
    ),
]
