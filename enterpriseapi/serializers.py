from rest_framework import serializers
from .models import Enterprise, Code

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'