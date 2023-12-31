# Generated by Django 4.2.4 on 2023-08-18 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0004_rename_desctiption_genre_description_game_studio'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game_collection', to=settings.AUTH_USER_MODEL, verbose_name='Author of the collection')),
                ('games_list', models.ManyToManyField(blank=True, related_name='game_collection', to='games.game')),
                ('likes', models.ManyToManyField(related_name='liked_collections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
