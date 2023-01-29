from rest_framework import serializers
from .models import Fruits

class FruitsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fruits 
		fields = ['id','name','calories']