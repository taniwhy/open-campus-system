# Generated by Django 2.1.5 on 2019-11-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('family_name', models.CharField(max_length=50, verbose_name='名前')),
                ('first_name', models.CharField(max_length=50, verbose_name='苗字')),
                ('family_name_reading', models.CharField(max_length=50, verbose_name='名前フリガナ')),
                ('first_name_reading', models.CharField(max_length=50, verbose_name='苗字フリガナ')),
                ('birthday', models.DateField(verbose_name='生年月日')),
                ('gender', models.BooleanField(verbose_name='性別')),
                ('phone_number', models.CharField(max_length=10, verbose_name='電話番号')),
                ('postal_code', models.CharField(max_length=7, verbose_name='郵便番号')),
                ('street_address', models.CharField(max_length=50, verbose_name='住所')),
                ('address', models.CharField(max_length=50, verbose_name='番地')),
                ('job', models.BooleanField(verbose_name='職業')),
                ('school', models.CharField(max_length=50, null=True, verbose_name='高校名')),
                ('school_year', models.IntegerField(null=True, verbose_name='学年')),
                ('graduate_year', models.CharField(max_length=50, null=True, verbose_name='卒業予定年')),
                ('graduated_check', models.BooleanField(null=True, verbose_name='高校卒業済み')),
                ('graduate_qualification', models.BooleanField(null=True, verbose_name='高認取得済み')),
            ],
            options={
                'db_table': 'participant',
            },
        ),
    ]