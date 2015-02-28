from nacho.models import Restaurant
from nacho.serializers import RestaurantSerializer
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django.contrib.auth.models import User
from nacho.serializers import UserSerializer
from rest_framework import permissions

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
	serializer_class = RestaurantSerializer
	# We do this, even though get_queryset is used, so that we can
	# generate the base_name
	queryset = Restaurant.objects.none()
	# Permission settings for accessing Restaurants
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		queryset = Restaurant.objects.all()
		latitude = self.request.QUERY_PARAMS.get('latitude', None)
		longitude = self.request.QUERY_PARAMS.get('longitude', None)
		distance = self.request.QUERY_PARAMS.get('distance', None)
		queryset = self.search(queryset, latitude, longitude, distance)
		return queryset

	def search(self, queryset, latitude, longitude, distance):
		if latitude is None or longitude is None:
			return queryset
		try:
			distance = float(distance)
		except:
			distance = 5

		dsq = distance * distance
		queryset = queryset.extra(where=["(latitude - %s) * (latitude - %s) + (longitude - %s) * (longitude - %s) <= %s"], 
			params=[latitude, latitude, longitude, longitude, dsq])
		return queryset

	def perform_create(self, serializer):
   		serializer.save(createdBy=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)