from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.food_details, name='food-details'),
    path('<int:item_id>/update/', views.update_food, name='update-item'),
    path('<int:item_id>/delete/', views.delete_food, name='delete-item'),
    path('add/', views.create_food, name='add-item'),
]