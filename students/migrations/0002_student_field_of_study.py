# Generated by Django 5.0.7 on 2024-07-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='field_of_study',
            field=models.CharField(default="Bachelor's Degree", max_length=50),
            preserve_default=False,
        ),
    ]