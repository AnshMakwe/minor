# Generated by Django 4.0.1 on 2022-04-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='value',
            field=models.CharField(blank=True, choices=[('Teacher', 'as a teacher'), ('Student', 'as a student')], max_length=200, null=True),
        ),
    ]
