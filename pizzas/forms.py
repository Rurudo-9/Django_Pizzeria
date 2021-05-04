from django import forms
from .models import Pizza, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        lable = {'name: ':''}
    
class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        lable = {'name: ':''}
        widgets = {'name':forms.Textarea(attrs={'cols':80})}
        
    
