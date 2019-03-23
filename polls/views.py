from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Poll, Choice, Vote
from django.http import JsonResponse
from .serializers import PollSerializer

# Create your views here.


# Pure django API endpoints without rest framework

def polls_list(request):
	polls = Poll.objects.all()[:20]
	data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
	return JsonResponse(data)

def polls_detail(request, pk):
	poll = get_object_or_404(Poll, pk = pk)
	data = {"results": {"question": poll.question,"created_by": poll.created_by.username,"pub_date": poll.pub_date}}
	return JsonResponse(data)

# check with 
# "curl http://localhost:8000/polls"
# "curl http://localhost:8000/polls/1"

###########################################


