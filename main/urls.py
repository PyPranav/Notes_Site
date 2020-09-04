from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home-page"),
    path('signup', views.signup, name='signup-page'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('new_dashboard', views.new_dashboard, name='new_dashboard'),
    path('save', views.save, name='save')
]