# Generated by Django 2.0.7 on 2018-07-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketsystem',
            name='Comment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]