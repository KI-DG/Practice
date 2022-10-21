from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

from .models import Article, Comment
# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        seriailzer = ArticleListSerializer(articles, many=True)
        return Response(seriailzer.data)
    
    elif request.method == 'POST':
        seriailzer = ArticleSerializer(data=request.data)
        if seriailzer.is_valid(raise_exception=True):
            seriailzer.save()
            return Response(seriailzer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        seriailzer = ArticleSerializer(article)
        return Response(seriailzer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        seriailzer = ArticleSerializer(article, data=request.data)
        if seriailzer.is_valid(raise_exception=True):
            seriailzer.save()
            return Response(seriailzer.data)

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        seriailzer = CommentSerializer(comments, many=True)
        return Response(seriailzer.data)



@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        seriailzer = CommentSerializer(comment)
        return Response(seriailzer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        seriailzer = CommentSerializer(comment, data=request.data)
        if seriailzer.is_valid(raise_exception=True):
            seriailzer.save()
            return Response(seriailzer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    seriailzer = CommentSerializer(data=request.data)
    if seriailzer.is_valid(raise_exception=True):
        seriailzer.save(article=article)
        return Response(seriailzer.data, status=status.HTTP_201_CREATED)