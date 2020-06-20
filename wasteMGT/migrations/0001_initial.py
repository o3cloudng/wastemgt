# Generated by Django 2.2.13 on 2020-06-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Waste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=20)),
                ('operatorID', models.CharField(max_length=20)),
                ('pickup_time', models.DateTimeField()),
                ('pickup_long', models.IntegerField(max_length=20)),
                ('pickup_lat', models.IntegerField(max_length=20)),
            ],
        ),
    ]