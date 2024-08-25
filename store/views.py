from django.views.generic import TemplateView,ListView

from articles.models import Article, Category


# Home page view content
class HomeView(TemplateView):
    template_name = 'store/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('-created')[:4]
        context['categories'] = Category.objects.all()
        return context


# catalog page view content

class CatalogView(ListView):
    model = Article

