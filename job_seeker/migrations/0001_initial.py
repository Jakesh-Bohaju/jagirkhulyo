# Generated by Django 2.2.3 on 2019-08-06 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.validator
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_auto_20190803_1622'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SeekerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[home.validator.name_validation])),
                ('address', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(validators=[home.validator.date_of_birth_validation])),
                ('phone_no', models.CharField(blank=True, max_length=9, validators=[home.validator.phone_no_validation])),
                ('mobile_no', models.CharField(blank=True, max_length=10, null=True, validators=[home.validator.mobile_no_validation])),
                ('resume', models.FileField(upload_to='resume/', verbose_name='')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='job_seeker/', verbose_name='')),
                ('slug', models.SlugField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_detail_district', to='home.District')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_detail_education', to='home.Education')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_detail_gender', to='home.Gender')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_detail_province', to='home.Province')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_detail_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
