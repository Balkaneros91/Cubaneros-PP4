from django.urls import path
from .views import MenuListView, MealDetailsView

app_name = 'menu'

urlpatterns = [
    path('', MenuListView.as_view(), name='menu'),
    path('meal/<slug:slug>/', MealDetailsView.as_view(), name='meal_details'),
]
