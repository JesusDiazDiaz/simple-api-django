from rest_framework.viewsets import ModelViewSet
from .models import Movies, Categories
from .serializers import MoviesSerializer, CategoriesSerializer


class MoviesViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class CategoriesViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
