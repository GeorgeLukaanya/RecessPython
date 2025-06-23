from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_views, name='login'),
    path('signup/', views.signup_views, name='signup'),
    path('detect/', views.detect_views, name='detect'),
    path('about/', views.about_views, name='about'),
]