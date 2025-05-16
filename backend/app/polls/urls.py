from os import name
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("create", views.create, name="create"),
    path("get", views.get_poll, name="get_poll"),
    path("getList", views.get_poll_list, name="get_poll_list"),
    path("update", views.update_poll, name="update_poll"),
    path("delete", views.delete_poll, name="delete_poll"),
]
