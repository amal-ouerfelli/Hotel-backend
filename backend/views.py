from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response
from backend.models import Chambres, Client
from backend.serializers import ChambresSerializer, ClientSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404, JsonResponse

# Create your views here.
@api_view(['GET'])
def test(request):
    chambres=Chambres.objects.all()
    serializer=ChambresSerializer(chambres, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def client(request):
    if (request.method=="POST"):
        serializers=ClientSerializer(data=request.data) #serialisation des données saisies
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=200) # retourne reponse json 

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)