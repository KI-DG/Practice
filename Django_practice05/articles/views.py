from django.shortcuts import render, redirect
from django.views.decorators.http import (
    require_safe,
    require_http_methods,
    require_POST,
)
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    # articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context ={
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
# new 와 create를 합친다 method를 통해 나누어진다
def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # new
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

    # form = ArticleForm(request.POST)
    # # form = ArticleForm(data = request.POST) data가 생략
    # if form.is_valid(): # 인스턴스 메서드
    #     # 통과 되면 True 못하면 False (검증과정이 추가) 검사가 간단함 그럴려고 form을 만듬
    #     article = form.save()
    #     # 새 글을 반환
    #     return redirect('articles:detail', article.pk )
    # # print(f'에러: {form.errors}')
    # context = {
    #     'form' : form,
    # }
    # return render(request, 'articles/new.html', context)
    # # return redirect('articles:new')

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # POST를 바꿔주는데 안된다. 안되는 이유는 주소에 값이 안나오고 HTTP body에 저장

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()

    # return render(request, 'articles/index.html')
    # index를 요청한게 아니라 아무것도 안뜨는것이다.
    # 주소가 변하지 않는다
    # render는 화면만 띄우기만 하기 때문에
    # return redirect('articles:index')
    # 위에 두가지 문제를 한번에 해결
    # 요청은 제대로 들어가고 길을 다시 찾아준다.
    # return redirect('articles:detail', article.pk)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 키=인자로 들어온 값
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context ={
#         'article' : article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

    # article = Article.objects.get(pk=pk)
    # form = ArticleForm(request.POST, instance=article)
    # if form.is_valid():
    #     form.save()
    #     return redirect('articles:detail', article.pk)
    # context ={
    #     'form': form
    # }
    # return render(request, 'articles/edit.html', context)

    # article.title = request.POST.get('title')
    # #'내가 바꾸고 싶은 제목'
    # article.content = request.POST.get('content')
    # #"내가 바꾸고 싶은 내용"
    # article.save()

    # return redirect('articles:detail', article.pk)
