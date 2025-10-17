from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated 
from .models import Doctor_Profile ,Appointments ,Prescription, Prescription_Item , PatientNotes 
from .serializer import Doctor_ProfileSerializer , AppointmentsSerializer , PrescriptionSerializer ,Prescription_ItemSerializer , PatientNotesSerializer 

class Doctor_Profileviews(viewsets.ModelViewSet):
    queryset = Doctor_Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = Doctor_ProfileSerializer 

class Appointmentsviews(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AppointmentsSerializer 

class Prescriptionviews(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PrescriptionSerializer 
class Prescription_Itemviews(viewsets.ModelViewSet):
    queryset = Prescription_Item.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = Prescription_ItemSerializer
class PatientNotesviews(viewsets.ModelViewSet):
    queryset = PatientNotes.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PatientNotesSerializer 

# Create your views here.
