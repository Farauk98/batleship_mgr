# Generated by Django 3.2.25 on 2024-07-20 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_gamesession'),
    ]

    operations = [
        migrations.AddField(
            model_name='shot',
            name='game_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shots', to='game.gamesession'),
        ),
    ]
