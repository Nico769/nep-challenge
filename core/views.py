from django.http import JsonResponse
from rest_framework import status, views
from rest_framework.response import Response

from .models import Node, Resource
from .serializers import NodeSerializer, ResourceSerializer


class ResourceAPIView(views.APIView):
    serializer_class = ResourceSerializer

    def get(self, request, id):
        # Silence pylint false positive check against the resource identifier
        # pylint: disable=redefined-builtin
        try:
            to_retrieve = Resource.objects.get(pk=id)
            serializer = ResourceSerializer(to_retrieve)
            return Response(serializer.data)
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

    def post(self, request):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        # Silence pylint false positive check against the resource identifier
        # pylint: disable=redefined-builtin
        try:
            to_modify = Resource.objects.get(pk=id)
            serializer = ResourceSerializer(to_modify, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Resource.DoesNotExist:
            return JsonResponse({"reason": "The resource does not exist"}, status=status.HTTP_404_NOT_FOUND)


class NodeAPIView(views.APIView):
    serializer_class = NodeSerializer

    def get(self, request, id):
        # Silence pylint false positive check against the resource identifier
        # pylint: disable=redefined-builtin
        try:
            to_retrieve = Node.objects.get(pk=id)
            serializer = NodeSerializer(to_retrieve)
            return Response(serializer.data)
        except Resource.DoesNotExist:
            return JsonResponse({"reason": "The resource does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, id=None):
        serializer = NodeSerializer(data=request.data, context={"parentNodeId": id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        # Silence pylint false positive check against the resource identifier
        # pylint: disable=redefined-builtin
        try:
            to_modify = Node.objects.get(pk=id)
            serializer = NodeSerializer(to_modify, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Resource.DoesNotExist:
            return JsonResponse({"reason": "The resource does not exist"}, status=status.HTTP_404_NOT_FOUND)
