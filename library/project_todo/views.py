from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializer import ProjectModelSerializer, TodoModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from .todo_filter import TodoFilter, ProjectFilter
from urllib import response
from rest_framework import status, mixins, viewsets
from rest_framework.response import Response
from django_filters import rest_framework as filters

class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class TodoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilter
    filter_backends = (filters.DjangoFilterBackend)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filter_backends = ProjectFilter