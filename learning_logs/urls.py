"""定义learning_logs的URL模式"""

from django.urls import path, re_path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # /()/中的()表示捕获正则数据，
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path('new_topic/',views.new_topic,name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
            name='edit_entry'),
]
