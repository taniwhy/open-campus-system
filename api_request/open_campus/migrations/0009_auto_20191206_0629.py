# Generated by Django 2.1.5 on 2019-12-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_campus', '0008_auto_20191203_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='birthday',
            field=models.CharField(max_length=20, verbose_name='生年月日'),
        ),
    ]
