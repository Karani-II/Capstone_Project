from django.shortcuts import render
from rest_framework import viewsets ,status 
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import get_rxcui ,check_drug_interactions

from rest_framework.permissions  import IsAuthenticated 
from .serializer import Pharmacist_ProfileSerializer , prescription_handlingSerializer ,DrugsSerializer, InventoryItemSerializer,DrugBatchSerializer , Refill_appointmentSerializer
from .models import Pharmacist_Profile, prescription_handling, Drugs , InventoryItem , DrugBatch , Refill_appointment  

class Pharmacist_Profileview(viewsets.ModelViewSet):
    serializer_class = Pharmacist_ProfileSerializer 
    queryset = Pharmacist_Profile.objects.all()
    permission_classes = [IsAuthenticated]

class prescription_handlingview(viewsets.ModelViewSet):
    queryset = prescription_handling.objects.all()
    serializer_class = prescription_handlingSerializer
    permission_classes = [IsAuthenticated]

class Drugsview(viewsets.ModelViewSet):
    queryset = Drugs.objects.all()
    serializer_class = DrugsSerializer 
    permission_classes = [IsAuthenticated]

class InventoryItemview(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer 
    permission_classes = [IsAuthenticated]
    def restock(self, request, pk=None):
        item = self.get_object()
        amount = int(request.data.get('amount', 0))
        item.restock(amount)
        return Response({'message': 'Item restocked successfully'}, status=status.HTTP_200_OK)

class DrugBatchview(viewsets.ModelViewSet):
    queryset = DrugBatch.objects.all()
    serializer_Class = DrugBatchSerializer 
    permission_classes = [IsAuthenticated]

class Refill_appointmentview(viewsets.ModelViewSet):
    queryset = Refill_appointment.objects.all()
    serializer_class = Refill_appointmentSerializer 
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
def drug_interaction_check(request):
    drug_names = request.data.get('drugs', [])

    if len(drug_names) < 2:
        return Response({"error": "Please provide at least two drug names"}, status=400)

    rxcuis = []
    for name in drug_names:
        rxcui = get_rxcui(name)
        if rxcui:
            rxcuis.append(rxcui)
        else:
            return Response({"error": f"Could not find RxCUI for {name}"}, status=404)

    interactions = check_drug_interactions(rxcuis)
    return Response(interactions)












#Create your views here.
