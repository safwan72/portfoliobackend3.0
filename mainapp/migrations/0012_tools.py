# Generated by Django 5.1.2 on 2024-10-26 13:37

import mainapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_uploadimage_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=200)),
                ('description', models.TextField(max_length=100, verbose_name='description')),
                ('image', models.ImageField(blank=True, upload_to=mainapp.models.upload_tools)),
            ],
            options={
                'verbose_name_plural': 'Tools',
                'db_table': 'Tools',
            },
        ),
    ]