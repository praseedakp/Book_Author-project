# Generated by Django 5.0.1 on 2024-01-26 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0003_bookmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authormodel',
            name='count1',
        ),
    ]