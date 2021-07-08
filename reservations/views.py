from reservations.models import Reserve
from reservations.serializers import ReservationSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny




class ReservationView(ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reserve.objects.all()
    lookup_field = 'pk'
    permission_classes = (AllowAny, )


    