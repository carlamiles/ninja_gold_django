from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime
# Create your views here.
def index(request):
    print('*'*50)
    print('the index function is running')
    context = {
        'gold': request.session['gold'],
        'activity': request.session['activity']
    }
    if 'activity' not in request.session:
        request.session['activity'] = []
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'ninja_gold_app/index.html', context)

def process_money(request):
    print('*'*50)
    print('the process money function is running')
    if request.POST['building'] == 'farm':
        money = random.randint(10, 20)
        request.session['gold'] += money #farm gives between 10-20 gold
        request.session['activity'].append(f"Earned {str(money)} gold from {request.POST['building']}! ({str(datetime.now())})")
    if request.POST['building'] == 'cave':
        money = random.randint(5, 10)
        request.session['gold'] += money #cave gives between 5-10 gold
        request.session['activity'].append(f"Earned {str(money)} gold from {request.POST['building']}! ({str(datetime.now())})")
    if request.POST['building'] == 'house':
        money = random.randint(2, 5)
        request.session['gold'] += money #house gives between 2-5 gold
        request.session['activity'].append(f"Earned {str(money)} gold from {request.POST['building']}! ({str(datetime.now())})")
    if request.POST['building'] == 'casino':
        win_or_lose = random.randint(0, 1)
        print(win_or_lose)
        money = random.randint(0, 50)
        if win_or_lose == 0: # casino gives/takes between 0 - 50 gold
            request.session['gold'] -= money 
            request.session['activity'].append(f"Lost {str(money)} gold from {request.POST['building']}! ({str(datetime.now())})")
        else:
            request.session['gold'] += money 
            request.session['activity'].append(f"Earned {str(money)} gold from {request.POST['building']}! ({str(datetime.now())})")
    return redirect('/')

def reset(request):
    print('*'*50)
    print('the process money function is running')
    request.session['activity'] = []
    request.session['gold'] = 0
    return redirect('/')