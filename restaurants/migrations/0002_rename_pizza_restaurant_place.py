# Generated by Django 3.2.6 on 2021-08-28 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='pizza',
            new_name='place',
        ),
    ]