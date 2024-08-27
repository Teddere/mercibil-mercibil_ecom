from django.views.generic import ListView
from django.shortcuts import render
from articles.models import Article,Category,ArticleImage


# Category list view content
class CategoryListView(ListView):
    pass

# category delete view content
def category_delete(request):
    pass