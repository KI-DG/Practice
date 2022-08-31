from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('greeting/', views.greeting, name = 'greeting'),
    path('throw/', views.throw, name = 'throw'),
    path('catch/', views.catch, name = 'catch'),
    # path('price/', views.price, name = 'price'),
    path('lotto/', views.lotto, name = 'lotto'),
]
