from django.contrib import admin
from django.urls import path
from . import views
from .apiviews import PollList, PollDetail, LoginView
from .class_views import PollListGeneric, PollDetailGeneric, CreateVote, ChoiceList, UserCreate, UserView

urlpatterns = [
	# Pure django api
    path('polls', views.polls_list, name = "polls_list"),
    path('polls/<int:pk>', views.polls_detail, name = "polls_detail"),
    # using DRF apiview
    path('poll_list', PollList.as_view(), name = "polls_list_api"),
    path('poll_detail/<int:pk>', PollDetail.as_view(), name = "polls_detail_api"),
    # using generic view
    path('poll_list_generic', PollListGeneric.as_view(), name = "polls_list_generic"),
    path('poll_detail_generic/<int:pk>', PollDetailGeneric.as_view(), name = "polls_detail_genric"),
    path("vote", CreateVote.as_view(), name = "create_vote"),
    path("choices", ChoiceList.as_view(), name = "choices"),
    path("users" , UserCreate.as_view(), name = "user_create"),
    path("user/view" , UserView.as_view(), name = "user_view"),
    path('login', LoginView.as_view(), name = "login"),

]
