from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserModelSerializer
from rest_framework.pagination import LimitOffsetPagination
class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100 



class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserLimitOffsetPagination


