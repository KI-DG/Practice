from django.shortcuts import render, redirect

import articles
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    # articles = Article.objects.order_by('-pk')
    context ={
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    #POST를 바꿔주는데 안된다. 안되는 이유는 주소에 값이 안나오고 HTTP body에 저장
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    # return render(request, 'articles/index.html')
    # index를 요청한게 아니라 아무것도 안뜨는것이다.
    # 주소가 변하지 않는다
    # render는 화면만 띄우기만 하기 때문에 
    # return redirect('articles:index')
    # 위에 두가지 문제를 한번에 해결 
    #요청은 제대로 들어가고 길을 다시 찾아준다.
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
                                # 키=인자로 들어온 값
    context ={
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context ={
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request,pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    #'내가 바꾸고 싶은 제목'
    article.content = request.POST.get('content')
    #"내가 바꾸고 싶은 내용"
    article.save()
    
    return redirect('articles:detail', article.pk)