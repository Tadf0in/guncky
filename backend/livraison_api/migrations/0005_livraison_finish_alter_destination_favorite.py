# Generated by Django 4.2.6 on 2023-10-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraison_api', '0004_alter_livraison_status_alter_livraison_taille'),
    ]

    operations = [
        migrations.AddField(
            model_name='livraison',
            name='finish',
            field=models.BooleanField(default=False, verbose_name='Terminée'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='favorite',
            field=models.BooleanField(default=False, verbose_name='Favoris'),
        ),
    ]
