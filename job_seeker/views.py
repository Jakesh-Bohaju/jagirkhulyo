from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView

from blog.models import Blog
from job_seeker.forms import ResumeForm
from job_seeker.models import SeekerDetail
from home.models import Gender, Education
from company.models import *


class SeekerDashboardBaseView(TemplateView):
    template_name = '_job_seeker_dashboard_base_2.html'
    model = SeekerDetail
    success_url = reverse_lazy('job_seeker:seeker_dashboard_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            context['seeker'] = SeekerDetail.objects.get(user_id=user)
        except Exception as e:
            print(e)
        return context


class SeekerDashboardIndexView(TemplateView):
    template_name = 'job_seeker_dashboard.html'
    model = SeekerDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            context['user'] = SeekerDetail.objects.get(user_id=user)
            context['seeker'] = SeekerDetail.objects.get(user_id=user)
        except Exception as e:
            print(e)
        return context


class JobListView(ListView):
    template_name = 'job_list.html'
    model = JobPost
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['jobs'] = JobPost.objects.all()
        user = self.request.user
        try:
            context['seeker'] = SeekerDetail.objects.get(user_id=user)
        except Exception as e:
            print(e)

        context['categories'] = Category.objects.all()
        context['top_jobs'] = JobPost.objects.all().order_by('?')
        context['latest_jobs'] = JobPost.objects.all().order_by('-id')
        context['freq_categories'] = Category.objects.all().order_by('?')
        context['blogs'] = Blog.objects.all().order_by('?')[:3]
        context['job_by_locations'] = JobPost.objects.all()
        return context


class CategoryListView(ListView):
    template_name = 'job_category.html'
    model = Category
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = Category.objects.all()
        user = self.request.user
        context['seeker'] = SeekerDetail.objects.get(user_id=user)
        context['freq_categories'] = Category.objects.all().order_by('?')
        context['blogs'] = Blog.objects.all().order_by('?')[:3]
        context['job_by_locations'] = JobPost.objects.all()
        context['top_jobs'] = JobPost.objects.all().order_by('?')
        return context


class JobDetailView(DetailView):
    model = JobPost
    template_name = 'single_job.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        job = JobPost.objects.get(slug=slug)
        context['job'] = job
        context['blogs'] = Blog.objects.all().order_by('?')[:3]
        context['job_by_locations'] = JobPost.objects.all()
        context['top_jobs'] = JobPost.objects.all().order_by('?')
        context['company'] = CompanyDetail.objects.get(job_post_company=job)
        user = self.request.user
        try:
            context['seeker'] = SeekerDetail.objects.get(user_id=user)
        except Exception as e:
            print(e)
        return context


class SeekerDetailView(CreateView):
    template_name = 'seeker_detail.html'
    model = SeekerDetail
    # fields = ['name', 'address', 'date_of_birth', 'phone_no','resume','image']
    form_class = ResumeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genders'] = Gender.objects.all()
        context['education'] = Education.objects.all()
        context['provinces'] = Province.objects.all()
        context['districts'] = District.objects.all()
        user = self.request.user
        try:
            context['seeker'] = SeekerDetail.objects.get(user_id=user)
        except Exception as e:
            print(e)
        return context

    def post(self, request, *args, **kwargs):
        # form = self.get_form()
        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():
            seeker_detail = form.save(commit=False)
            seeker_detail.user = request.user
            gender = request.POST.get('gend')
            education = request.POST.get('educ')
            province = request.POST.get('province')
            district = request.POST.get('district')
            gen = Gender.objects.get(gender=gender)
            edu = Education.objects.get(education=education)
            prov = Province.objects.get(province_name=province)
            dis = District.objects.get(district=district)
            seeker_detail.gender_id = gen.id
            seeker_detail.education_id = edu.id
            seeker_detail.province_id = prov.id
            seeker_detail.district_id = dis.id
            seeker_detail.save()

            return redirect('job_seeker:job_list')

        else:
            print(form.errors)

        return redirect('job_seeker:seeker_detail')


class SeekerUpdateView(UpdateView):
    model = SeekerDetail
    fields = ['name', 'province', 'district', 'address', 'date_of_birth', 'gender', 'phone_no', 'mobile_no', 'education', 'resume', 'image']
    template_name = 'seeker_update_form.html'
    success_url = reverse_lazy('job_seeker:seeker_dashboard_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            context['seeker'] = SeekerDetail.objects.get(user_id=user)
        except Exception as e:
            print(e)
        return context


class SeekerAppliedView(ListView):
    model = ReceivedResume
    template_name = 'job_applied.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            context['applied_list'] = ReceivedResume.objects.filter(applicant_name__user=user)
            context['seeker'] = SeekerDetail.objects.get(user_id=user)
        except Exception as e:
            print(e)
        return context


class ChangePasswordView(PasswordChangeView):
    template_name = 'password_change_form.html'
    success_url = reverse_lazy('job_seeker:seeker_dashboard_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            context['seeker'] = SeekerDetail.objects.get(user_id=user)
        except Exception as e:
            print(e)
        return context
