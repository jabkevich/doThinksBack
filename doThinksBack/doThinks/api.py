from rest_framework import viewsets, permissions
from .serializers import *


class GroupViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Group.objects.all()
        owner = self.request.query_params.get('owner', None)
        if owner is not None:
            queryset = queryset.filter(owner=owner)
        return queryset

    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer


class TaskViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Task.objects.all()
        group = self.request.query_params.get('group', None)
        print(group)
        if group is not None:
            queryset = queryset.filter(group=group)
            queryset = queryset.order_by('priority')
        return queryset

    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = TaskSerializer


class PointViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Point.objects.all()
        group = self.request.query_params.get('group', None)
        if group is not None:
            queryset = queryset.filter(group=group)
        return queryset

    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PointSerializer
