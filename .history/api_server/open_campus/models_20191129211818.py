from django.db import models


class Participant(models.Model):

    class Meta:
        db_table = "参加者"
    id = models.AutoField(primary_key=True)
    family_name = models.CharField(verbose_name="名前", max_length=50)
    first_name = models.CharField(verbose_name="苗字", max_length=50)
    family_name_reading = models.CharField(verbose_name="名前フリガナ", max_length=50)
    first_name_reading = models.CharField(verbose_name="苗字フリガナ", max_length=50)
    birthday = models.DateField(verbose_name="生年月日", auto_now=False, auto_now_add=False)
    gender = models.BooleanField(verbose_name="性別")
    phone_number = models.PhoneNumberField()