import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

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
    return render(request, 'greeting.html', context)

def throw(request):
    return render(request, 'throw.html')

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
    return render(request, 'catch.html', context)

def lotto(request):
    name = '기룡'
    
    context ={
        'name': name
    }
    return render(request, 'lotto.html', context)