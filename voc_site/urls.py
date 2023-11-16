from django.urls import path

from voc_site import views

urlpatterns = [
    path("home", views.home_page, name = "home"),
    path("", views.home_page),
    path("words_list", views.table, name = "table"),
    path("add_word", views.add_word, name ="add_word")
]