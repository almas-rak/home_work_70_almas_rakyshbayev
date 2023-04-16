from rest_framework import serializers

from issue_tracker.models import Project, Task


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'created_at', 'completed_at')


class ProjectTasks(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'summary')
        read_only_field = ('id', 'summary')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'created_at', 'completed_at')
        read_only_fields = ('id',)


class ProjectDetailSerializer(serializers.ModelSerializer):
    tasks = ProjectTasks(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'completed_at', 'tasks')
        read_only_fields = ('id', 'tasks')
