from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:item_id>/', views.FoodDetailView.as_view(), name='food-details'),
    path('<int:item_id>/update/', views.update_food, name='update-item'),
    path('<int:item_id>/delete/', views.delete_food, name='delete-item'),
    path('add/', views.FoodCreateView.as_view(), name='add-item'),
]