from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator

def article_list(request):
    articles = Article.published.all()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'article_list.html', {'page_obj':page_obj})
