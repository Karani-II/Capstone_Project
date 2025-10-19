from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient_Profile 
from.serializer import Patient_ProfileSerializer 
from rest_framework.permissions import IsAuthenticated 

class Patient_Profileview(viewsets.ModelViewSet):
    queryset = Patient_Profile.objects.all()
    serializer_class = Patient_ProfileSerializer 
    permission_classes = [IsAuthenticated]
    


# Create your views here.
