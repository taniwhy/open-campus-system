from django.db import models


class Participant(models.Model):

    class Meta:
        db_table = "参加者"
    id = models.AutoField(primary_key=True)
    first_name= models.CharField(_("aa"), max_length=50)