from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from nacho import views

router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),

]