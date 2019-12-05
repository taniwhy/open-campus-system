from rest_framework import routers, SimpleRouters
from .views import ParticipantList, ParticipantDetail, ParticipantHistoryViewSet, SubjectList

router = SimpleRouter(trailing_slash=False)

router.register(r'participant', ParticipantList)
router.register(r'participant_detail', ParticipantDetail)
router.register(r'participant_history', ParticipantHistoryViewSet)
router.register(r'subject', SubjectList)