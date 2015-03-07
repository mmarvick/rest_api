from collections import OrderedDict
from rest_framework import viewsets, mixins
from rest_framework.response import Response

class HeadedListModelMixin(mixins.ListModelMixin):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
    	response = mixins.ListModelMixin.list(self, request, *args, **kwargs);
    	data = self.get_params()
    	data['results'] = response.data
        return Response(data)

class HeadedModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   HeadedListModelMixin,
                   viewsets.GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass