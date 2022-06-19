from django.contrib import admin
from blog.models import Article, Category, Comment


admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)