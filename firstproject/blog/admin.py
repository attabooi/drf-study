from django.contrib import admin
from blog.models import Article, Category


admin.site.register(Category)
admin.site.register(Article)