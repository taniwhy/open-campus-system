from django.db import models

class Subject(models.Model):
    """
    学科テーブル
    """
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(verbose_name="学科名", max_length=50)

    class Meta:
        db_table = "subject"

    def __str__(self):
        return self.subject_name


class Participant(models.Model):
    """
    参加者テーブル
    """
    id = models.AutoField(primary_key=True)
    family_name = models.CharField(verbose_name="名前", max_length=50)
    first_name = models.CharField(verbose_name="苗字", max_length=50)
    family_name_reading = models.CharField(verbose_name="名前フリガナ", max_length=50)
    first_name_reading = models.CharField(verbose_name="苗字フリガナ", max_length=50)
    birthday = models.CharField(verbose_name="生年月日", max_length=20)
    gender = models.BooleanField(verbose_name="性別")
    phone_number = models.CharField(verbose_name="電話番号", max_length=11)
    postal_code = models.CharField(verbose_name="郵便番号", max_length=7)
    street_address = models.CharField(verbose_name="住所", max_length=50)
    address = models.CharField(verbose_name="番地", max_length=50)
    job = models.BooleanField(verbose_name="職業")
    school_name = models.CharField(verbose_name="高校名", max_length=50, blank=True, null=True)
    school_year = models.CharField(verbose_name="学年", max_length=10, blank=True, null=True)
    graduate_year = models.CharField(verbose_name="卒業予定年", max_length=50, blank=True, null=True)
    graduated_check = models.NullBooleanField(verbose_name="高校卒業済み")
    graduate_qualification = models.NullBooleanField(verbose_name="高認取得済み")

    class Meta:
        db_table = "participant"

    def __str__(self):
        return self.family_name + self.first_name


class ParticipantHistory(models.Model):
    """
    参加者履歴テーブル
    """
    participant = models.ForeignKey(Participant, verbose_name="参加者", on_delete=models.CASCADE)
    join_subject = models.CharField(verbose_name="参加学科", max_length=50)
    join_day = models.CharField(verbose_name="参加日", max_length=15, default="nulpo",)
    school_year = models.CharField(verbose_name="学年", max_length=10, default="nulpo",)

    class Meta:
        db_table = "participant_history"