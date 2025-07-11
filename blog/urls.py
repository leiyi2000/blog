from django.urls import path

from .api.ping import ping
from .api.article import read


urlpatterns = [
    path("ping", ping),
    path("article/<int:article_id>", read),
]
