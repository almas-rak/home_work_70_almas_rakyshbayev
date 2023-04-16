from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.task_serializers import TaskSerializer, TaskCreateSerializer, TaskDetailSerializer
from issue_tracker.models import Task


class TaskAPIView(APIView):

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            tasks_objects = Task.objects.get_or_none(pk=kwargs.get('pk'))
            if not tasks_objects:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            tasks = TaskDetailSerializer(tasks_objects)
        else:
            tasks_objects = Task.objects.all().order_by('id')
            tasks = TaskSerializer(tasks_objects, many=True)
        return Response(tasks.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            tasks_objects = Task.objects.get_or_none(pk=kwargs.get('pk'))
            if not tasks_objects:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            serializer = TaskCreateSerializer(data=request.data, instance=tasks_objects)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'answer': 'NO pk in request'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            tasks_objects = Task.objects.get_or_none(pk=kwargs.get('pk'))
            if not tasks_objects:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            serializer = TaskCreateSerializer(data=request.data, instance=tasks_objects, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'answer': 'NO pk in request'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            task = Task.objects.get_or_none(pk=kwargs.get('pk'))
            if not task:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            task.delete()
            return Response({'answer': 'deleted'}, status=status.HTTP_200_OK)
        return Response({'answer': 'NO pk in request'}, status=status.HTTP_400_BAD_REQUEST)
