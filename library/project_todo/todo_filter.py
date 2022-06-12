from dataclasses import field
from pyexpat import model
from unicodedata import name
from django_filters import rest_framework as filters
from .models import Project, ToDo

class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='project_name', lookup_expr="contains")

    class Meta:
        model = Project
        fields = ['project_name']



class TodoFilter(filters.FilterSet):
    
    class Meta:
        model = ToDo
        fields = ['project_name_todo']