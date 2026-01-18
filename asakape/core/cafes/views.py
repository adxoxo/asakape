from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Cafe
from .serializers import CafeSerializer
# Create your views here.
class CafeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = Cafe.objects.all()

    serializer_class = CafeSerializer

