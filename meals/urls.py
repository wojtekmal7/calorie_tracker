from django.urls import path
from .views import AddMealView, MealListView, RegisterView, CustomLoginView, UserProfileView, HomePageView, logout_view, meals_for_date
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('add/<str:date>/', AddMealView.as_view(), name='add_meal'),
    path('list/', MealListView.as_view(), name='meal_list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('', HomePageView.as_view(), name='home'),
    path('meals/delete/<int:meal_id>/', views.delete_meal, name='delete_meal'),
    path('logout/', logout_view, name='logout'),
    path('meals/<str:date>/', views.meals_for_date, name='meals_for_date'),
]
