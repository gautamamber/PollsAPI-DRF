from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('polls', views.polls_list, name = "polls_list"),
    path('polls/<int:pk>', views.polls_detail, name = "polls_detail")
]
