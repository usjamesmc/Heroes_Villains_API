from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super_Type
from .models import Super 

@api_view(['GET', 'POST'])
def super_list(request):  
    super_types = Super_Type.objects.all()
    custom_response_dictionary = {}
    if request.method == 'GET':
        for super_type in super_types:
            supers = Super.objects.filter(super_type_id = super_type.id)
            super_serializer = SuperSerializer(supers, many = True)
            custom_response_dictionary[super_type.type] = {
            '':super_serializer.data
            }
        return Response(custom_response_dictionary)
    elif request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])       
def super_detail(request, pk):
    super = get_object_or_404(Super, pk = pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super); 
        return Response(serializer.data) 
    elif request.method == 'PUT':
       serializer = SuperSerializer(super, data = request.data) 
       serializer.is_valid(raise_exception = True)
       serializer.save()
       return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def hero_list(request):
    super_type_param = request.query_params.get('super_type')
    heroes = Super.objects.filter(super_type = 'Hero')
    if request.method == 'GET' and super_type_param == 'Hero':
        serializer = SuperSerializer(heroes, many = True)
        return Response(serializer.data)