# Generated by Django 5.1 on 2024-12-07 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_remove_sheet_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='salary',
        ),
    ]
