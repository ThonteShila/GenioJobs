# Generated by Django 4.2.2 on 2023-08-01 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geniojobsapp', '0014_remove_applied_jobs_genio_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applied_jobs',
            old_name='job_seeker_profile_id',
            new_name='Job_Seeker_Profile_id',
        ),
    ]
