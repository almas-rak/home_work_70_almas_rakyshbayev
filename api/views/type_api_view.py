from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import TypeSerializer
from issue_tracker.models import Type


class TypeAPIView(APIView):

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            try:
                type_objects = Type.objects.get(pk=kwargs.get('pk'))
            except Type.DoesNotExist:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            type_object = TypeSerializer(type_objects)
            return Response(type_object.data, status=status.HTTP_200_OK)
        else:
            type_objects = Type.objects.all().order_by('id')
            type_object = TypeSerializer(type_objects, many=True)
        return Response(type_object.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            try:
                type_objects = Type.objects.get(pk=kwargs.get('pk'))
            except Type.DoesNotExist:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            serializer = TypeSerializer(data=request.data, instance=type_objects)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'answer': 'NO pk in request'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            try:
                type_objects = Type.objects.get(pk=kwargs.get('pk'))
            except Type.DoesNotExist:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            serializer = TypeSerializer(data=request.data, instance=type_objects, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'answer': 'NO pk in request'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            try:
                type_objects = Type.objects.get(pk=kwargs.get('pk'))
            except Type.DoesNotExist:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            type_objects.delete()
            return Response({'answer': 'deleted'}, status=status.HTTP_200_OK)
        return Response({'answer': 'NO pk in request'}, status=status.HTTP_400_BAD_REQUEST)