# Generated by Django 3.1 on 2020-08-28 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nx', '0004_auto_20200828_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=280)),
                ('logo', models.ImageField(upload_to='Finance')),
                ('description', models.TextField()),
                ('alias', models.CharField(max_length=280)),
                ('type', models.IntegerField()),
                ('wallet_type', models.IntegerField()),
                ('currency', models.CharField(max_length=280)),
                ('commission', models.CharField(max_length=280)),
                ('gateway_fees', models.CharField(max_length=280)),
            ],
        ),
    ]