from rest_framework import serializers
from .models import *


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    point = PointSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'title', 'owner', 'task')
