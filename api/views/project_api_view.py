from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProjectSerializer, ProjectDetailSerializer
from issue_tracker.models import Project


class ProjectAPIView(APIView):
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            project_objects = Project.objects.get_or_none(pk=kwargs.get('pk'))
            if not project_objects:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            projects = ProjectDetailSerializer(project_objects)
        else:
            project_objects = Project.objects.all().order_by('id')
            projects = ProjectSerializer(project_objects, many=True)
        return Response(projects.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProjectDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            project_objects = Project.objects.get_or_none(pk=kwargs.get('pk'))
            if not project_objects:
                return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
            serializer = ProjectDetailSerializer(data=request.data, instance=project_objects)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        project_objects = Project.objects.get_or_none(pk=kwargs.get('pk'))
        if not project_objects:
            return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
        serializer = ProjectDetailSerializer(data=request.data, instance=project_objects, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        project = Project.objects.get_or_none(pk=kwargs.get('pk'))
        if not project:
            return Response({'answer': 'NO CONTENT'}, status=status.HTTP_204_NO_CONTENT)
        project.delete()
        return Response({'answer': 'deleted'}, status=status.HTTP_200_OK)

