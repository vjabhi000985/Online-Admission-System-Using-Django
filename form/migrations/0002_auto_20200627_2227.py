# Generated by Django 3.0.4 on 2020-06-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appform',
            name='date_of_birth',
            field=models.CharField(max_length=12),
        ),
    ]
