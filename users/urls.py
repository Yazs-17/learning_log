"""定义users的URL模式"""
"""为应用程序users定义URL模式"""
# users/urls.py
from django.urls import path,re_path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'urls'
urlpatterns = [
    # 登录页面
    path('login/', LoginView.as_view(template_name='users/login.html'),
            name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^register/$', views.register, name='register'),
]
