# Generated by Django 4.0.4 on 2022-05-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_course_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(upload_to='media/course'),
        ),
    ]
