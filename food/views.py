from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm

# Create your views here.


def index(request):
    items = Food.objects.all()
    context = {
        'items': items
    }
    return render(request, 'food/index.html', context)


def food_details(request, item_id):
    item = Food.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'food/food_details.html', context)


def create_food(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/food_form.html', {'form': form})


def update_food(request, item_id):
    item = Food.objects.get(pk=item_id)
    print(item)
    form = FoodForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/food_form.html', {'form': form})

def delete_food(request, item_id):
    item = Food.objects.get(pk=item_id)
    if request.method == 'POST':
        if request.POST['delete'] == 'confirm':
            item.delete()
            return redirect('food:index')
        else:
            return redirect('food:food-details', item_id=item_id)
    
    return render(request, 'food/food_delete.html', {'item':item})