# Generated by Django 4.1.3 on 2022-11-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_forumsubcategories_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumsubcategories',
            name='logo',
        ),
        migrations.AddField(
            model_name='forumcategory',
            name='logo',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
