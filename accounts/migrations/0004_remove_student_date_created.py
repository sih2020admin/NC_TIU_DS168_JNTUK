# Generated by Django 3.0.8 on 2020-08-02 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200731_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_created',
        ),
    ]
