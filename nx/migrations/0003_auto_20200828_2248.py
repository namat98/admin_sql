# Generated by Django 3.1 on 2020-08-28 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nx', '0002_auto_20200828_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='login',
            field=models.CharField(max_length=240, unique=True),
        ),
    ]
