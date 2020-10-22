# Generated by Django 3.1.2 on 2020-10-14 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20201007_1813'),
        ('student', '0005_auto_20201008_2234'),
        ('employmentform', '0001_initial'),
        ('careerform', '0001_initial'),
        ('appointments', '0003_auto_20201014_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='attachment1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='attachment2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='attachment3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='cc_form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='careerform.careercounselorform'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='ec_form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employmentform.employmentconsultantform'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='staff_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staffaccount'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='staff_notes',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='student_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.studentaccount'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='student_notes',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
