# Generated by Django 4.1 on 2022-09-06 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servidor',
            name='reglamento',
        ),
    ]
