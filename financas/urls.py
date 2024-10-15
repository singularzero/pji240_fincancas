from django.urls import path
from . import views  # Deve referenciar as views no mesmo diretório

urlpatterns = [
    path('categoria/', views.categoriaApi),  # Para listar todas as categorias
    path('categoria/<int:id>/', views.categoriaApi)  # Para acessar uma categoria específica
]
