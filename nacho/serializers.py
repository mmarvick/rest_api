from rest_framework import serializers
from nacho.models import Restaurant
from django.contrib.auth.models import User

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
	createdBy = serializers.ReadOnlyField(source="createdBy.username")
	
	class Meta:
		model = Restaurant
		fields = ('url', 'createdBy', 'name', 'phone', 'address', 'city',
				 'stateProvince', 'zip', 'latitude', 'longitude',
				  'happyHourStart', 'happyHourEnd')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	restaurants = serializers.PrimaryKeyRelatedField(many=True, queryset=Restaurant.objects.all())

	class Meta:
		model = User
		fields = ('url', 'username', 'is_superuser', 'restaurants')