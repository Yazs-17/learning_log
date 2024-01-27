from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    return render(request,'learning_logs/index.html')

def topics(request):
    """
    显示所有的主题
    """
    topics = Topic.objects.order_by('date_added')
    # 上下文是一个字典，其中的键是我们将在模板中用来访问数据的名称，
    # 而值是我们要发送给模板的数据。
    context = {'toplist':topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')#-表示按降序排列，即先显示最近的条目
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():#判断用户填写是否有效
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
