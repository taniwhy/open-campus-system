from django.db import models

class Participant(models.Model):
    class meta:
        db_table = 'participant'
    participant_id = models.UUIDField(verbose_name='ID', primary_key=True)
    first_name = models.CharField(verbose_name='名前',max_length=16)
    last_name = models.CharField(verbose_name='苗字',max_length=16)
    first_name_reading = models.CharField(verbose_name='名前フリガナ',max_length=32)
    last_name_reading = models.CharField(verbose_name='苗字フリガナ',max_length=32)
    birthday = models.DateField(verbose_name='生年月日')
    gender = models.BooleanField(verbose_name='性別')
    phone_number = models.CharField(verbose_name='電話番号', max_lengh=11)
    postal_code = models.CharField(verbose_name='郵便番号', max_length=7)
    address = models.CharField(max_length=128)
    job = models.BooleanField()
    highschool_id = models.UUIDField(_("高校ID"))
