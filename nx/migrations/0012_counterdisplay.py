# Generated by Django 3.1 on 2020-08-29 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nx', '0011_delete_heroproxyusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='CounterDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]