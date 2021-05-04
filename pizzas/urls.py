from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('menu/<int:pizza_id>', views.pizza, name='pizza'),
    path('new_pizza/', views.new_pizza, name='new_pizza'),
    path('new_topping/<int:pizza_id>/', views.new_topping, name='new_topping'),
    path('edit_topping/<int:topping_id>/', views.edit_topping, name='edit_topping'),
    path('comments/<int:pizza_id>/', views.comments, name='comments'),
]