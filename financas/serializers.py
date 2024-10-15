from rest_framework import serializers
from financas.models import Categoria, Gastos, Receitas

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id',
                  'nome')
        
class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gastos
        fields = ('id',
                  'categoria',
                  'retirado_em',
                  'valor')
        
class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = ('id',
                  'categoria',
                  'adicionado_em',
                  'valor')