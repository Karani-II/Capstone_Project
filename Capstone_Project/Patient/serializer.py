from rest_framework import serializers 
from .models import Patient_Profile 

class Patient_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Profile 
        fields = '__all__'
