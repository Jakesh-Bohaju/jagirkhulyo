# Generated by Django 2.2.3 on 2019-08-06 07:21

from django.db import migrations, models
import home.validator
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('company_type', models.CharField(max_length=100)),
                ('phone_no', models.CharField(blank=True, max_length=9, validators=[home.validator.phone_no_validation])),
                ('mobile_no', models.CharField(blank=True, max_length=10, null=True, validators=[home.validator.mobile_no_validation])),
                ('company_description', models.TextField()),
                ('company_registration_date', models.DateField(blank=True, null=True, validators=[home.validator.registration_date_validation])),
                ('company_image', sorl.thumbnail.fields.ImageField(upload_to='company/', verbose_name='')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('vacancy_no', models.IntegerField()),
                ('experience', models.CharField(max_length=15)),
                ('salary', models.IntegerField(blank=True)),
                ('negotiable', models.BooleanField(blank=True)),
                ('description', models.TextField()),
                ('job_requirement', models.TextField()),
                ('pub_date', models.DateField(auto_now=True)),
                ('deadline', models.DateField(validators=[home.validator.deadline_validation])),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='ReceivedResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateField(auto_now=True)),
                ('status', models.BooleanField(blank=True)),
                ('accepted', models.BooleanField(blank=True)),
            ],
        ),
    ]
