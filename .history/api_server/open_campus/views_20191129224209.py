from rest_framework import mixins
from rest_framework import viewsets

from .models import Goods
from .serializer import GoodsSerializer


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
     queryset = Goods.objects.all()
     serializer_class = GoodsSerializer