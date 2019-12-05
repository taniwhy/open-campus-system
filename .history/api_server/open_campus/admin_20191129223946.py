from django.contrib import admin

from .models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['code', 'mobile', "add_time"]


admin.site.register(VerifyCode, VerifyCodeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)