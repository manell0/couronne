# Generated by Django 3.2.7 on 2021-09-24 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='snitt',
            new_name='average',
        ),
    ]