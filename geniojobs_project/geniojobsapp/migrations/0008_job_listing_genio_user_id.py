# Generated by Django 4.2.2 on 2023-07-06 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geniojobsapp', '0007_job_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_listing',
            name='genio_user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='geniojobsapp.geniousers'),
        ),
    ]