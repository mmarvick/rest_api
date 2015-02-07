from rest_framework import serializers
from nacho.models import Restaurant

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Restaurant
		fields = ('url', 'name', 'phone', 'address', 'city', 'stateProvince', 'zip', 'latitude', 'longitude', 'happyHourStart', 'happyHourEnd')