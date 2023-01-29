from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Fruits
from .serializers import FruitsSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class FruitList(APIView):
	def get(self, request):
		queryset = Fruits.objects.all()
		serializer = FruitsSerializer(
			queryset, many=True, context={'request': request})
		return Response(serializer.data)

	def post(self, request):
		serializer = FruitsSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class FruitDetail(APIView):
	def get(self, request, id):
		fruit = get_object_or_404(Fruits, pk=id)
		serializer = FruitsSerializer(fruit)
		return Response(serializer.data)

	def put(self, request, id):
		fruit = get_object_or_404(Fruits, pk=id)
		serializer = FruitsSerializer(fruit, data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

	def delete(self, request, id):
		fruit = get_object_or_404(Fruits, pk=id)
		fruit.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)