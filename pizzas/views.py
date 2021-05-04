from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pizza, Comment
from .forms import PizzaForm,ToppingForm
from django.http import Http404

# Create your views here.

def index(request):
    '''The home page for pizzeria'''
    return render(request, 'pizzas/index.html')

@login_required
def menu(request):
    menu = Pizza.objects.order_by('date_added')

    context = {'menu': menu}

    return render(request,'pizzas/menu.html', context)

@login_required
def pizza(request,pizza_id):

    pizza = Pizza.objects.get(id=pizza_id)
    Toppings = pizza.topping_set.order_by('-date_added')
  

    context = {'pizza': pizza, 'Toppings': Toppings}
    return render(request, 'pizzas/pizza.html',context)

def new_pizza(request):
    if request.method != 'POST': 
        form = PizzaForm()

    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save() # save to database directly

            return redirect("pizzas:menu")
    context= {'form':form}
    return render(request, "pizzas/new_pizza.html", context)

@login_required
def new_topping(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if pizza.owner != request.user:
        raise Http404

    if request.method !='POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)

        if form.is_valid():
            new_topping = form.save(commit=False) 
            new_topping.pizza = pizza
            new_topping.save()
            form.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)
    
    context = {'form': form, 'pizza': pizza}
    return render(request, 'pizzas/new_topping.html', context)

@login_required
def edit_topping(request, topping_id):
    toppings = Toppings.objects.get(id=topping_id)
    pizza = toppings.pizza

    if pizza.owner != request.user:
        raise Http404

    if request.method !='POST':
        form = ToppingForm(instance=toppings)
    else:
        form = ToppingForm(instance=toppings, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)
    
    context = {'toppings': toppings, 'pizza':pizza,'form': form}
    return render(request, 'pizzas/edit_topping.html', context)

def comments(request,pizza_id):
    if request.method != 'POST' and request.POST.get('btn1'):
        comment = request.POST.get('comment')
        Comment.objects.create(pizza_id=pizza_id, username=request.user, text=comment, date_added=date.today)
        comments = Comment.objects.filter(pizza=pizza_id)
        pizza = Pizza.objects.get(id=pizza_id)

        context = {'pizza':pizza, 'comments': comments}
        return render(request, 'pizzas/comments.html',context)




