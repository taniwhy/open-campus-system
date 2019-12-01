from rest_framework import viewsets, routers
from .models import Participant
from .serializers import ParticipantSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)