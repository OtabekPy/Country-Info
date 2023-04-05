from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class ContinentsAPIViewSet(ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer

    def get_queryset(self):
        continents = Continent.objects.all()
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = continents.filter(name__icontains=search)
        else:
            return continents
        return queryset


class CountriesAPIViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        countrys = Country.objects.all()
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = countrys.filter(name__icontains=search) | countrys.filter(
                capital__icontains=search) | countrys.filter(
                continent__in=Continent.objects.filter(name__contains=search))
        else:
            return countrys
        return queryset


class ContiguousAPIViewSet(ModelViewSet):
    queryset = Contiguous.objects.all()
    serializer_class = ContiguousSerializer

    def get_queryset(self):
        contiguos = Contiguous.objects.all()
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = Contiguous.objects.filter(country__in=Country.objects.filter(name__icontains=search))
        else:
            return contiguos
        return queryset
