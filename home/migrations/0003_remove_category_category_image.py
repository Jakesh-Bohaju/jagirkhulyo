# Generated by Django 2.2.3 on 2019-08-29 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_image',
        ),
    ]
