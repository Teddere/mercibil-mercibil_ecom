from django.contrib import admin
from articles.models import Category,Article,ArticleImage


admin.site.register(Category)
admin.site.register(Article)
admin.site.register(ArticleImage)
