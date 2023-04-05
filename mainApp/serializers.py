from rest_framework.serializers import ModelSerializer
from .models import *


class ContinentSerializer(ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CountryNameSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class ContiguousSerializer(ModelSerializer):

    country = CountryNameSerializer()
    countrys = CountryNameSerializer(many=True)

    class Meta:
        model = Contiguous
        fields = '__all__'
