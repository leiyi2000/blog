from django.urls import path

from .api.ping import ping
from .api.article import reads


urlpatterns = [
    path("ping", ping),
    path("article/access/reads", reads),
]
