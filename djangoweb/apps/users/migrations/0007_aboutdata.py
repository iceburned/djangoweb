# Generated by Django 4.1.3 on 2022-12-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_appuser_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=255)),
            ],
        ),
    ]