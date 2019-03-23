from django.contrib import admin
from django.urls import path
from . import views
from .apiviews import PollList, PollDetail

urlpatterns = [
	# Pure django api
    path('polls', views.polls_list, name = "polls_list"),
    path('polls/<int:pk>', views.polls_detail, name = "polls_detail"),
    # using DRF apiview
    path('poll_list', PollList.as_view(), name = "polls_list_api"),
    path('poll_detail/<int:pk>', PollDetail.as_view(), name = "polls_detail_api"),
]
