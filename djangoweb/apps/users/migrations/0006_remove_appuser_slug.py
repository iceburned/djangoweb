# Generated by Django 4.1.3 on 2022-12-07 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_appuser_avatar_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='slug',
        ),
    ]