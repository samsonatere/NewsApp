from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

class HomePageView(TemplateView):
    template_name = 'home.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    model = Profile
    template_name = 'profile.html'