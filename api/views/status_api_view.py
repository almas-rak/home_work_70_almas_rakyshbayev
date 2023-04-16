from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import StatusSerializer
from issue_tracker.models import Status


class StatusAPIView(APIView):

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            try:
                status_objects = Status.objects.get(pk=kwargs.get('pk'))
            except Status.DoesNotExist:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            status_object = StatusSerializer(status_objects)
            return Response(status_object.data, status=status.HTTP_200_OK)
        else:
            status_objects = Status.objects.all().order_by('id')
            status_object = StatusSerializer(status_objects, many=True)
        return Response(status_object.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            try:
                status_objects = Status.objects.get(pk=kwargs.get('pk'))
            except Status.DoesNotExist:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            serializer = StatusSerializer(data=request.data, instance=status_objects)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'answer': 'NO pk in request'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            try:
                status_objects = Status.objects.get(pk=kwargs.get('pk'))
            except Status.DoesNotExist:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            serializer = StatusSerializer(data=request.data, instance=status_objects, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'answer': 'NO pk in request'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            try:
                status_objects = Status.objects.get(pk=kwargs.get('pk'))
            except Status.DoesNotExist:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            status_objects.delete()
            return Response({'answer': 'deleted'}, status=status.HTTP_200_OK)
        return Response({'answer': 'NO pk in request'}, status=status.HTTP_400_BAD_REQUEST)

