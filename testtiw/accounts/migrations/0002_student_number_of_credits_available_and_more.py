# Generated by Django 5.0.2 on 2024-08-23 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='number_of_credits_available',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='number_of_credits_required',
            field=models.IntegerField(default=0),
        ),
    ]
