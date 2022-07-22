# Generated by Django 3.2.14 on 2022-07-22 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_document_is_free'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_module_name', models.CharField(max_length=100)),
                ('can_view', models.BooleanField(default=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.document')),
            ],
        ),
        migrations.DeleteModel(
            name='CourseModule',
        ),
    ]
