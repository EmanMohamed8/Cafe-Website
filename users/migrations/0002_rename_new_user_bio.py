# Generated by Django 4.1.1 on 2023-07-19 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='new',
            new_name='bio',
        ),
    ]
