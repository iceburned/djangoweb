# Generated by Django 4.1.3 on 2022-12-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('forum', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='forumsubcategories',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='forumtopic',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
