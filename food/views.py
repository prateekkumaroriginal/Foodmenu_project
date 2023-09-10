from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.


class IndexView(ListView):
    model = Food
    template_name = 'food/index.html'
    context_object_name = 'items'

class FoodDetailView(DetailView):
    model = Food
    pk_url_kwarg = 'item_id'
    context_object_name = 'item'
    template_name = 'food/food_details.html'


class FoodCreateView(CreateView):
    model = Food
    fields = ['name', 'desc', 'price', 'image_url']
    template_name = 'food/food_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



def create_food(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/food_form.html', {'form': form})


def update_food(request, item_id):
    item = Food.objects.get(pk=item_id)
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

    return render(request, 'food/food_delete.html', {'item': item})
