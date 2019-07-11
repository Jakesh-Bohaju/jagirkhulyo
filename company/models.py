import os
import random

from django.utils.text import slugify

from sorl.thumbnail import ImageField

from custom_auth.models import User
from django.db import models

# Create your models here.
from home.models import *
from job_seeker.models import SeekerDetail


class CompanyDetail(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    company_type = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    company_image = ImageField(upload_to='company/', verbose_name="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        value = self.company_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class JobPost(models.Model):
    title = models.CharField(max_length=100)
    job_level = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vacancy_no = models.IntegerField()
    experience = models.CharField(max_length=15)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    salary = models.IntegerField()
    description = models.TextField()
    pub_date = models.DateField(auto_now=True)
    deadline = models.DateField()
    company = models.ForeignKey(CompanyDetail, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        random_number = random.randint(1000, 1000000)
        value = self.company.company_name + ' ' + self.title + ' ' + str(random_number)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class ReceivedResume(models.Model):
    job_title = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    applicant_name = models.ForeignKey(SeekerDetail, on_delete=models.CASCADE)
    applied_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.applicant_name

