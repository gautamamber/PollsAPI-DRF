from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Poll, Choice, Vote
from django.http import JsonResponse
from .serializers import PollSerializer
from rest_framework import status

# Create your views here.
###########################################

# RestFramework views
# APIVIEWS



class PollList(APIView):
	def get(self, request):
		polls = Poll.objects.all()[:20]
		data = PollSerializer(polls, many = True).data
		return Response(data)

	def post(self, request, format = None):
		serializer = PollSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PollDetail(APIView):
	def get(self,request, pk):
		poll = get_object_or_404(Poll , pk = pk)
		data = PollSerializer(poll).data
		return Response(data)


	def put(self, request, format = None):
		serializer = PollSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		