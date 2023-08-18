# Generated by Django 4.2.4 on 2023-08-18 06:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gamecollection',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='gamecollection',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_collections', to=settings.AUTH_USER_MODEL),
        ),
    ]
