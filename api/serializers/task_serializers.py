from rest_framework import serializers

from api.serializers.status_serializers import StatusSerializer
from api.serializers.type_serializers import TypeSerializer
from issue_tracker.models import Task, Project, Status, Type


class TaskProjectSerialize(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name')
        read_only_fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    project = TaskProjectSerialize(read_only=True)
    status = StatusSerializer(read_only=True)
    type = TypeSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'summary', 'status', 'type', 'project', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at', 'project')


class TaskDetailSerializer(serializers.ModelSerializer):
    project = TaskProjectSerialize(read_only=True)
    status = StatusSerializer(read_only=True)
    type = TypeSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'summary', 'status', 'type', 'description', 'project', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at', 'project')


class TaskCreateSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    type = serializers.PrimaryKeyRelatedField(many=True, queryset=Type.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'summary', 'description', 'status', 'type', 'project', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
