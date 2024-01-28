from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#Just 模型告诉Django如何处理程序中存储的数据
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    #https://docs.djangoproject.com/en/1.8/ref/models/fields
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        #https://docs.djangoproject.com/en/5.0/
        if len(self.text)<50:
            return self.text
        return self.text[:50]+"..."









    
