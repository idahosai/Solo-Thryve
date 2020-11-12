# Generated by Django 3.1.2 on 2020-10-23 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='careercounselorform',
            name='ccs_cover',
        ),
        migrations.RemoveField(
            model_name='careercounselorform',
            name='ccs_interview',
        ),
        migrations.RemoveField(
            model_name='careercounselorform',
            name='ccs_jobsearch',
        ),
        migrations.RemoveField(
            model_name='careercounselorform',
            name='ccs_mockinterview',
        ),
        migrations.RemoveField(
            model_name='careercounselorform',
            name='ccs_networking',
        ),
        migrations.RemoveField(
            model_name='careercounselorform',
            name='ccs_portfolio',
        ),
        migrations.RemoveField(
            model_name='careercounselorform',
            name='ccs_resume',
        ),
        migrations.AddField(
            model_name='careercounselorform',
            name='ccs_cplanning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='careercounselorform',
            name='ccs_eplanning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='careercounselorform',
            name='ccs_exploration',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='careercounselorform',
            name='ccs_labourmarket',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='careercounselorform',
            name='ccs_other',
            field=models.BooleanField(default=False),
        ),
    ]
