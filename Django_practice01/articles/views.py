import datetime
from email import message
import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['apple', 'chicken', 'burger']
    six_food = [food for food in foods if len(food) > 6]
    today = datetime.datetime(2022, 8, 8, 10, 2)

    context ={
        'name': 'justin',
        'foods': foods,
        'six_food': six_food,
        'today' : today,
    }
    return render(request, 'articles/greeting.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # print(request)
    # print(type(request))
    # print(request.GET)
    department = request.GET.get('department')
    name = request.GET.get('name')

    if department == '대전 2반':
        if name == '이기용':
            message = '교육생이시군요'
        else: 
            message = '교수님이시군요'
    else:
        message = '다른 반이시군요'

    context ={
        'message': message
    }
    return render(request, 'articles/catch.html', context)

# def price(request):
#     product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
#     if product_price == '라면':
#         message = product_price.values * 
#     elif product_price == '홈런볼':
#     elif
#     context ={
#     'product_price' : product_price    
#     }
#     return render(request, 'price.html', context)

def lotto(request):
    name = '기룡'
    ran = random.sample(range(1,46), 6)
    context ={
        'name': name,
        'ran' : ran,
    }
    return render(request, 'articles/lotto.html', context)