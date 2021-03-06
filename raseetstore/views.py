from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import product
from . serializers import productSerializer


class productlist(APIView):
    def get(self, request):
        productdata = product.objects.all()
        serializer = productSerializer(productdata, many=True)
        return Response(serializer.data)
