# Generated by Django 3.1.3 on 2021-09-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheridan_id', models.CharField(max_length=10, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
            options={
                'unique_together': {('sheridan_id', 'password')},
            },
        ),
    ]
