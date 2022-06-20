from tkinter import CASCADE
from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone




# Create your models here.



class Category(models.Model):
    category = models.CharField(("카테고리 이름"), max_length=50, unique=True)
    description = models.CharField(("카테고리 설명"), max_length=200)
    
    def __str__(self):
        return self.category



class Article(models.Model):
    # def start_time():
    #     return datetime.today()
    
    # def end_time():
    #     return datetime.today() + timedelta(days=3)

    author = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(("글 제목"), max_length=200)
    body = models.CharField(("글 내용"), max_length=1000)
    category = models.ManyToManyField('Category')
    start_date = models.DateTimeField("게시글 노출 시작 일자", auto_now_add=True)



    # def clean(self):
    #     if not self.end_date:
    #         self.end_date = (self.start_date + timedelta(days=3))
    
    # def save(self, **kwargs):
    #     self.clean()
    #     return super().save(**kwargs)
    def __str__(self):
        return f'{self.author} : {self.title}'

class Comment(models.Model):
    author = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    article = models.ForeignKey('Article', verbose_name="게시물", on_delete=models.CASCADE)
    comment = models.CharField(("댓글 내용"), max_length=100)


