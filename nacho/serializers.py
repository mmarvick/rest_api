from rest_framework import serializers
from nacho.models import Restaurant
from django.contrib.auth.models import User

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Restaurant
		fields = ('url', 'name', 'phone', 'address', 'city', 'stateProvince', 'zip', 'latitude', 'longitude', 'happyHourStart', 'happyHourEnd')
		owner = serializers.HiddenField(source='owner.username')


class UserSerializer(serializer.HyperlinkedModelSerializer):
	restaraunt = serializers.PrimaryKeyRelatedField(many=True, querset=Restraunt.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'restaraunts')