from tkinter import CASCADE
from django.db import models

# Create your models here.



class Category(models.Model):
    category = models.CharField(("카테고리 이름"), max_length=50, unique=True)
    description = models.CharField(("카테고리 설명"), max_length=200)
    
    def __str__(self):
        return self.category

class Article(models.Model):
    author = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(("글 제목"), max_length=200)
    body = models.CharField(("글 내용"), max_length=1000)
    category = models.ManyToManyField('Category')

    def __str__(self):
        return f'{self.author} : {self.title}'

class Comment(models.Model):
    author = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    article = models.ForeignKey('Article', verbose_name="게시물", on_delete=models.CASCADE)
    comment = models.CharField(("댓글 내용"), max_length=100)


