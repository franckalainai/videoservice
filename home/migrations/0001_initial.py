# Generated by Django 4.0.4 on 2022-05-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_description', models.TextField()),
                ('is_premium', models.BooleanField(default=False)),
                ('course_image', models.ImageField(upload_to='course.png')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
