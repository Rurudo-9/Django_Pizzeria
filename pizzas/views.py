from django.shortcuts import render

from .models import Pizza, Comment

# Create your views here.

def index(request):
    '''The home page for pizzeria'''
    return render(request, 'pizzas/index.html')

def menu(request):
    menu = Pizza.objects.order_by('date_added')

    context = {'menu': menu}

    return render(request,'pizzas/menu.html', context)

def pizza(request,pizza_id):

    pizza = Pizza.objects.get(id=pizza_id)
    Toppings = pizza.topping_set.order_by('-date_added')
  

    context = {'pizza': pizza, 'Toppings': Toppings, 'comment_count_list': comment_count_list}
    return render(request, 'pizzas/pizza.html',context)

def comments(request,pizza_id):
    if request.method != 'POST' and request.POST.get('btn1'):
        comment = request.POST.get('comment')
        Comment.objects.create(pizza_id=pizza_id, username=request.user, text=comment, date_added=date.today)
        comments = Comment.objects.filter(pizza=pizza_id)
        pizza = Pizza.objects.get(id=pizza_id)

        context = {'pizza':pizza, 'comments': comments}
        return render(request, 'pizzas/comments.html',context)




