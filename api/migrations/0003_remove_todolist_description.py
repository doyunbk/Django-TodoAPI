# Generated by Django 3.0.4 on 2020-03-16 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200315_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='description',
        ),
    ]
