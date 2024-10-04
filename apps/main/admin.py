from django.contrib import admin
from apps.main.models import Category, Tag, Article, Comment, Like, Rating

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Rating)
