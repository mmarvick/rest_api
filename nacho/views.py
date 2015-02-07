from nacho.models import Restaurant
from nacho.serializers import RestaurantSerializer
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
	serializer_class = RestaurantSerializer
	# We do this, even though get_queryset is used, so that we can
	# generate the base_name
	queryset = Restaurant.objects.none()

	def get_queryset(self):
		queryset = Restaurant.objects.all()
		latitude = self.request.QUERY_PARAMS.get('latitude', None)
		longitude = self.request.QUERY_PARAMS.get('longitude', None)
		distance = self.request.QUERY_PARAMS.get('distance', None)
		if latitude is not None:
			queryset = queryset.filter(latitude=latitude)
		if longitude is not None:
			queryset = queryset.filter(longitude=longitude)
		return queryset