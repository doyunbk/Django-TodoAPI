# Generated by Django 3.0.4 on 2020-03-17 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200317_0735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='user',
            new_name='created_by',
        ),
    ]
