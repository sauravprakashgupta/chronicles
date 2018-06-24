from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'articles/article_list.html',{'all_articles':articles})
    
