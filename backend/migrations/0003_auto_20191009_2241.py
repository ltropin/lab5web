# Generated by Django 2.2.6 on 2019-10-09 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20191009_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='vahicle',
            new_name='vehicle',
        ),
    ]
