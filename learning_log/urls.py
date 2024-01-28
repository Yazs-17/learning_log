"""learning_log"""
from django.contrib import admin
from django.urls import path, include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls', namespace='learning_logs')),
    re_path(r'^users/',include('users.urls',namespace = 'users')),
]
