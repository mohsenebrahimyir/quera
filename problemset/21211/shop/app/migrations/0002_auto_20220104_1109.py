# Generated by Django 2.0.7 on 2022-01-04 11:09

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('available', django.db.models.manager.Manager()),
            ],
        ),
    ]
