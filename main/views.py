from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from .models import (
        UserProfile,
        Blog,
        Portfolio,
        Testimonial,
        Certificate
)

from django.views import generic

from . forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blog = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)


        context["testimonial"] = testimonials
        context["certification"] = certificates
        context["blogs"] = blog
        context["portfolio"] = portfolio
        return context


class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.sucess(self.request, 'Thank you. We will be in touch')
        return super().form_valid(form)



class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "main/portfolio-detal.html"

class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)    


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"
