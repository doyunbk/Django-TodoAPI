# Generated by Django 3.0.4 on 2020-03-17 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200317_0501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='created_by',
            new_name='user',
        ),
    ]