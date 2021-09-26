from django.shortcuts import render
from .models import Food
# Create your views here.
def index(request):
    food1 = Food()
    food1.name='Paneer Teeka'
    food1.price=80
    food1.desc='Paneer tikka is an Indian dish made from chunks of paneer marinated in spices and grilled in a tandoor'
    food1.img='gallery/01.jpg'

    food2 = Food()
    food2.name='Pizza'
    food2.price=130
    food2.desc='Pizza is a savory dish of Italian origin consisting of a usually round, flattened base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients'
    food2.img='gallery/02.jpg'

    food3 = Food()
    food3.name='Manchurian'
    food3.price=40
    food3.desc='Manchurian is a class of Indian Chinese dishes made by roughly chopping and deep-frying a main ingredient like chicken, cauliflower, prawn, fish, mutton or paneer cheese and then sautéeing it in a sauce flavored with soy sauce.'
    food3.img='gallery/05.jpg'

    food4 = Food()
    food4.name='Salad'
    food4.price=50
    food4.desc='Healthy Food to Eat!!!'
    food4.img='gallery/07.jpg'

    food = [food1,food2,food3,food4]

    return render(request,'index.html',{'food':food})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')