# Generated by Django 3.2.7 on 2021-09-24 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_matcher_userprofileinfo_best_ranking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='rating',
            new_name='number_played_matches',
        ),
    ]
