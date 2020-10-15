# Generated by Django 3.1.2 on 2020-10-15 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
        ('studentauth', '0001_initial'),
        ('student', '0005_auto_20201008_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentaccount',
            name='auth_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='studentauth.studentauth'),
        ),
        migrations.AlterField(
            model_name='studentaccount',
            name='program_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='program.schoolprogram'),
        ),
    ]
