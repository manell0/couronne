# Generated by Django 3.2.7 on 2021-09-24 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_snitt_userprofileinfo_average'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='matcher',
            new_name='best_ranking',
        ),
    ]
