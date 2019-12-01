from django.db import models


class Participant(models.Model):

    class Meta:
        db_table = "participant"
    id = models.AutoField(primary_key=True)
    family_name = models.CharField(verbose_name="名前", max_length=50)
    first_name = models.CharField(verbose_name="苗字", max_length=50)
    family_name_reading = models.CharField(verbose_name="名前フリガナ", max_length=50)
    first_name_reading = models.CharField(verbose_name="苗字フリガナ", max_length=50)
    birthday = models.DateField(verbose_name="生年月日", auto_now=False, auto_now_add=False)
    gender = models.BooleanField(verbose_name="性別")
    phone_number = models.CharField(verbose_name="電話番号", max_length=10)
    postal_code = models.CharField(verbose_name="郵便番号", max_length=7)
    street_address = models.CharField(verbose_name="住所", max_length=50)
    address = models.CharField(verbose_name="番地", max_length=50)
    job = models.BooleanField("職業")
    school = models.CharField(verbose_name="高校名", max_length=50)
    school_year = models.IntegerField(verbose_name="学年")
    graduate_year = models.CharField(verbose_name="卒業予定年", max_length=50)
    graduated_check = models.BooleanField("高校卒業済み")
    graduate_qualification = models.BooleanField(verbose_name="高認取得済み")