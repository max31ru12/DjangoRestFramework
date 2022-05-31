from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import ToDo, Project

class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"