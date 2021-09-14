from django.urls import path
from .views import HomePageView, ProfileView, profileSettings

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('settings/', profileSettings, name="settings"),
    ]