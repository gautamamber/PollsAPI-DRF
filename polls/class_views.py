from rest_framework import generics
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

# Generic classes
class PollListGeneric(generics.ListCreateAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer



class PollDetailGeneric(generics.RetrieveDestroyAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer