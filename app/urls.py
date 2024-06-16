from django.urls import path
from app import views
urlpatterns = [
    path('',views.Home),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin),
    path('logout',views.handleLogout),
    path('contact',views.contact),
    path('join',views.enroll),
    path('profile',views.profile),
    path('gallery',views.gallery),
    path('attendance',views.attendance),
]