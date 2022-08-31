from multiprocessing import context
from django.shortcuts import render
from .models import Article
def index(request):
    articles = Article.objects.all()
    context ={
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 사용자의데이터를 받아서 
    title = request.GET.get('title')
    content = request.GET.get('content')
    # DB에 저장 (3가지 방식)
    #1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    #2 사용은 이걸로 한다.
    article = Article(title=title, content=content)
    article.save()
    #3
    # Article.objects.create(title=title, content=content)


    return render(request, 'articles/create.html')