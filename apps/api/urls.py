from django.conf.urls import url, include
from rest_framework import routers
from apps.api import viewsets
from apps.api import views as api_view


from rest_framework.authtoken import views as rest_view


router = routers.DefaultRouter()
router.register(r'movies', viewsets.MoviesViewSet)
router.register(r'categories', viewsets.CategoriesViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', rest_view.obtain_auth_token),

    # vista con funciones
    url(r'^f-movies/$', api_view.movies_list),
    url(r'^f-movies/(?P<pk>[0-9]+)$', api_view.movies_detail),

    # vista con clases
    url(r'^categories-list/$', api_view.CategoriesList.as_view())
]
