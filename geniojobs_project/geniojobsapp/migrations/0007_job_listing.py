# Generated by Django 4.2.2 on 2023-07-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geniojobsapp', '0006_alter_geniousers_organization_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=200)),
                ('experience', models.IntegerField(default=0)),
                ('no_of_vacancies', models.IntegerField(default=1)),
                ('expiration_date', models.DateTimeField()),
            ],
        ),
    ]
