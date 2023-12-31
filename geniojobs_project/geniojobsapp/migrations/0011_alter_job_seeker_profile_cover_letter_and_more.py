# Generated by Django 4.2.2 on 2023-07-26 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geniojobsapp', '0010_alter_job_seeker_profile_genio_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='cover_letter',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='job_seeker_profile',
            name='genio_user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='geniojobsapp.geniousers'),
        ),
    ]
