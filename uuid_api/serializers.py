from rest_framework.serializers import ModelSerializer
from .models import the_Model
from rest_framework import serializers

class the_ModelSerializer(ModelSerializer):
    class Meta:
        model = the_Model
        fields = '__all__'