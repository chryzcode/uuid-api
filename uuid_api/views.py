from django.shortcuts import render
from .serializers import the_ModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import the_Model

# get all the_Models
@api_view(['GET'])
def get_all_the_Models(request):
    instance = the_Model.objects.create()
    instance.save()
    data = the_Model.objects.order_by('-time_stamp')
    response = {}
    for item in data:
        response[str(item.id)] = item.time_stamp
    return Response(response, status=200)