from rest_framework import serializers
from nacho.models import Restaurant
from django.contrib.auth.models import User

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Restaurant
		fields = ('url', 'name', 'phone', 'address', 'city', 'stateProvince', 'zip', 'latitude', 'longitude', 'happyHourStart', 'happyHourEnd')
		owner = serializers.HiddenField(default='owner.username')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	restaurants = serializers.PrimaryKeyRelatedField(many=True, queryset=Restaurant.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'restaurants')