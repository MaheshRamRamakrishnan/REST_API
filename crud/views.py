from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .models import*
from .serializers import drinkSerializer
from rest_framework.decorators import api_view
@api_view(['GET', 'POST'])
def drink_list(request):

    if request.method == 'GET':
     Drinks = drink.objects.all()
     serializer = drinkSerializer(Drinks , many=True)
     return JsonResponse({"drinks" : serializer .data}, safe=False)

    if request.method == 'POST':
        serializer = drinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def drink_detail(request):
    if request.method=='GET':
        pass
    elif request.method=='PUT':
        pass
    elif request.method=='DELETE':
        pass
