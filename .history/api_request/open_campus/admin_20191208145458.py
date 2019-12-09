from django.contrib import admin

from .models import Participant, ParticipantHistory, Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    pass

@admin.register(ParticipantHistory)
class ParticipantHistoryAdmin(admin.ModelAdmin):
    pass