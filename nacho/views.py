from nacho.models import Restaurant
from nacho.serializers import RestaurantSerializer
from nacho import customviewsets
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django.contrib.auth.models import User
from nacho.serializers import UserSerializer
from rest_framework import permissions
from collections import OrderedDict

# Create your views here.
class RestaurantViewSet(customviewsets.HeadedModelViewSet):
	serializer_class = RestaurantSerializer
	# We do this, even though get_queryset is used, so that we can
	# generate the base_name
	queryset = Restaurant.objects.none()
	# Permission settings for accessing Restaurants
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	# Search params
	distance = None;
	latitude = None;
	longitude = None;

	def get_queryset(self):
		queryset = Restaurant.objects.all()
		self.parse_params(self.request)
		queryset = self.search(queryset)
		return queryset

	def get_params(self):
		params = OrderedDict()
		params['latitude'] = self.latitude;
		params['longitude'] = self.longitude;
		params['distance'] = self.distance;
		return params

	def parse_params(self, request):
		latitude = self.request.QUERY_PARAMS.get('latitude', None)
		longitude = self.request.QUERY_PARAMS.get('longitude', None)
		distance = self.request.QUERY_PARAMS.get('distance', None)

		if latitude is None or longitude is None:
			self.latitude = None
			self.longitude = None
			self.distance = None
		else:
			try:
				distance = float(distance)
			except:
				distance = 5

			self.latitude = latitude
			self.longitude = longitude
			self.distance = distance

	def search(self, queryset):
		if self.latitude is None or self.longitude is None or self.distance is None:
			return queryset

		dsq = self.distance * self.distance
		queryset = queryset.extra(where=["(latitude - %s) * (latitude - %s) + (longitude - %s) * (longitude - %s) <= %s"], 
			params=[self.latitude, self.latitude, self.longitude, self.longitude, dsq])
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
