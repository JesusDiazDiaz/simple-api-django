from rest_framework.serializers import ModelSerializer
from .models import Movies, Categories


class MoviesSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'
        # profundidad de relaciones
        depth = 1


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
