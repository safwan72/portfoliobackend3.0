# Generated by Django 5.1.2 on 2024-10-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_projects_image_projects_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]