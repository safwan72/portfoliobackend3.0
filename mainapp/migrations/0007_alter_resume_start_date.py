# Generated by Django 5.1.2 on 2024-10-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_resume_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]