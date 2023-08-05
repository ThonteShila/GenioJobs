# Generated by Django 4.2.2 on 2023-07-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geniojobsapp', '0002_student_stud_add'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stud_add',
        ),
        migrations.AddField(
            model_name='student',
            name='is_current',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='stud_add1',
            field=models.CharField(default='address1 here', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='stud_add2',
            field=models.CharField(default='address2 here', max_length=20),
        ),
    ]
