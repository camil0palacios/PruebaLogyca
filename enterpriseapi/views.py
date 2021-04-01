# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser 

from .models import Enterprise, Code
from .serializers import EnterpriseSerializer, CodeSerializer

def Exeption_json():
    message = 'Not found'
    return JsonResponse({'message': message }, status=status.HTTP_404_NOT_FOUND)

# Especial querys

class AllEnterprise(APIView):
    def get(self, request):
        enterprises = Enterprise.objects.all()
        data = EnterpriseSerializer(enterprises, many=True)
        return JsonResponse(data.data, safe=False)

class EnterpriseByNit(APIView):
    def get(self, request, nit):
        try:
            enterprise = Enterprise.objects.get(Nit=nit)
            enterprise = EnterpriseSerializer(enterprise)
            codes = Code.objects.filter(Owner=enterprise.data['Id'])
            codes = CodeSerializer(codes, many=True)
            res = {'Enterprise': enterprise.data, 'codes': codes.data},
            return JsonResponse(res, safe=False)
        except:
            return Exeption_json()

class AllCodeById(APIView):
    def get(self, request, id):
        codes = Code.objects.filter(Owner=id)
        data = CodeSerializer(codes, many=True)
        return JsonResponse(data.data, safe=False)

class EnterpriseById(APIView):
    def get(self, request, id):
        try:
            code = Code.objects.get(Id=id)
            code = CodeSerializer(code)
            enterprise = Enterprise.objects.get(Id=code.data['Owner'])
            enterprise = EnterpriseSerializer(enterprise)
            return JsonResponse(enterprise.data, safe=False)
        except:
            return Exeption_json()

# CRUD Enterprise, Codes

class EnterpriseView(APIView):
    def get(self, request, id):
        try:
            enterprise = Enterprise.objects.get(Id=id)
            data = EnterpriseSerializer(enterprise)
            return JsonResponse(data.data, safe=False)
        except:
            return Exeption_json()

    def post(self, request):
        enterprise = JSONParser().parse(request)
        data = EnterpriseSerializer(data=enterprise)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        try:
            enterprise = Enterprise.objects.get(Id=id)
            enterprise_data = JSONParser().parse(request)
            data = EnterpriseSerializer(enterprise, data=enterprise_data, partial=True)
            if data.is_valid():
                data.save()
                return JsonResponse(data.data, status=status.HTTP_200_OK)
            return JsonResponse(data.errors, status=status.HTTP_400_BAD_REQUEST) 
        except:
            return Exeption_json()

class CodeView(APIView):
    def get(self, request, id):
        try:
            code = Code.objects.get(Id=id)
            data = CodeSerializer(code)
            return JsonResponse(data.data, safe=False)
        except:
            return Exeption_json()

    def post(self, request):
        code = JSONParser().parse(request)
        data = CodeSerializer(data=code)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        try:
            code = Code.objects.get(Id=id)
            code_data = JSONParser().parse(request)
            data = CodeSerializer(code, data=code_data, partial=True)
            if data.is_valid():
                data.save()
                return JsonResponse(data.data, status=status.HTTP_200_OK)
            return JsonResponse(data.errors, status=status.HTTP_400_BAD_REQUEST) 
        except:
            return Exeption_json()