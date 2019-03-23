from rest_framework import generics
from .models import Poll, Choice

from django.contrib.auth.models import User
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer
from rest_framework import status
# Generic classes





class UserCreate(generics.CreateAPIView):
	authentication_classes = ()
	permission_classes = ()
	serializer_class = UserSerializer

class UserView(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class PollListGeneric(generics.ListCreateAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer



class PollDetailGeneric(generics.RetrieveDestroyAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
	queryset = Choice.objects.all()
	serializer_class = ChoiceSerializer

class CreateVote(generics.CreateAPIView):
	serializer_class = VoteSerializer