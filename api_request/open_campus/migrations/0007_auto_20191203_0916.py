# Generated by Django 2.1.5 on 2019-12-03 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_campus', '0006_auto_20191203_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='graduate_qualification',
            field=models.BooleanField(blank=True, null=True, verbose_name='高認取得済み'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='graduate_year',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='卒業予定年'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='graduated_check',
            field=models.BooleanField(blank=True, null=True, verbose_name='高校卒業済み'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='school_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='高校名'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='school_year',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='学年'),
        ),
    ]