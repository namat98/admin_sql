# Generated by Django 3.1 on 2020-08-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nx', '0005_finance'),
    ]

    operations = [
        migrations.AddField(
            model_name='finance',
            name='display',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finance',
            name='extra_fees',
            field=models.CharField(default=1, max_length=280),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finance',
            name='max',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finance',
            name='min',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finance',
            name='processing',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finance',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
