# Generated by Django 5.1 on 2024-11-28 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_remove_department_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='salary',
        ),
    ]
