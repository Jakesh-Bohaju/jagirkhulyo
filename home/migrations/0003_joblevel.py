# Generated by Django 2.2.3 on 2019-08-01 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_jobtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_level', models.CharField(max_length=20)),
            ],
        ),
    ]