from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializer import ProjectModelSerializer, TodoModelSerializer
from rest_framework.pagination import LimitOffsetPagination

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100

class TodoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination