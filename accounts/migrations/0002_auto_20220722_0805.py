# Generated by Django 3.2.14 on 2022-07-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donnees',
            name='annee',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='donnees',
            name='ethnie',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='donnees',
            name='population',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='donnees',
            name='nom',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='donnees',
            name='structure',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
