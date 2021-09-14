from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .form import ProfileForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    model = Profile
    template_name = 'profile.html'

def profileSettings(request):
	profile = request.user
	form = ProfileForm(instance=profile)

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES,instance=profile)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'profile_setting.html', context)