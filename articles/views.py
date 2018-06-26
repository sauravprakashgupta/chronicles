from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'articles/article_list.html',{'all_articles':articles})

def article_detail(request, slug):
    articles = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html',{'article':articles})
