# Generated by Django 3.2.7 on 2022-04-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movie',
        ),
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(related_name='actors', to='movies.Movie'),
        ),
    ]
