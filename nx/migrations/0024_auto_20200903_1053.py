# Generated by Django 3.1 on 2020-09-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nx', '0023_auto_20200903_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'В ожидании'), (2, 'Обработано')], null=True),
        ),
    ]
