# Generated by Django 4.0.4 on 2022-05-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_coursemodule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(upload_to='course'),
        ),
    ]