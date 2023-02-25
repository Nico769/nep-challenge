from django.http import JsonResponse
from rest_framework import status, views
from rest_framework.response import Response

from .models import Resource
from .serializers import ResourceSerializer


class ResourceAPIView(views.APIView):
    serializer_class = ResourceSerializer

    def get_serializer_context(self):
        return {"request": self.request, "format": self.format_kwarg, "view": self}

    def get_serializer(self, *args, **kwargs):
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def get(self, request, id):
        # Silence pylint false positive check against the resource identifier
        # pylint: disable=redefined-builtin
        try:
            to_retrieve = Resource.objects.get(pk=id)
            to_retrieve_ser = ResourceSerializer(to_retrieve)
            return Response(to_retrieve_ser.data)
        except Resource.DoesNotExist:
            return JsonResponse({"reason": "The resource does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        # Silence pylint false positive check against the resource identifier
        # pylint: disable=redefined-builtin
        try:
            to_delete = Resource.objects.get(pk=id)
            to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Resource.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
