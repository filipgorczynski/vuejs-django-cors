from django.conf.urls import include, url

from .views import top_rated

urlpatterns = [
    url(r'^$', top_rated, name='top-rated'),
]