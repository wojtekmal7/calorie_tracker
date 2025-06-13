from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Meal
from .forms import MealForm
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm, UserProfileForm
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
import datetime

class AddMealView(View):
    def get(self, request, date):
        form = MealForm()
        return render(request, 'meals/add_meal.html', {'form': form, 'date': date})

    def post(self, request, date):
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.date = date
            meal.save()
            return redirect('meals_for_date', date=date)
        return render(request, 'meals/add_meal.html', {'form': form, 'date': date})


class MealListView(View):
    def get(self, request):
        meals = Meal.objects.filter(user=request.user)
        selected_date = request.GET.get('date', '')
        print(f"Selected date: {selected_date}")
        return render(request, 'meals/meal_list.html', {'meals': meals, 'selected_date': selected_date})

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'meals/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_profile')
        return render(request, 'meals/register.html', {'form': form})



class CustomLoginView(LoginView):
    template_name = 'meals/login.html'

class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserProfileForm(instance=request.user)
        meal_list_url = reverse('meal_list')

        context = {
            'form': form,
            'meal_list_url': meal_list_url,
        }
        return render(request, 'meals/user_profile.html', context)

    def post(self, request):
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        meal_list_url = reverse('meal_list')
        context = {
            'form': form,
            'meal_list_url': meal_list_url,
        }
        return render(request, 'meals/user_profile.html', context)

class HomePageView(View):
    def get(self, request):
        return render(request, 'meals/home.html')

def delete_meal(request, meal_id):
    if request.method == 'POST':
        try:
            meal = Meal.objects.get(pk=meal_id)
            meal.delete()
            return JsonResponse({'success': True})
        except Meal.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Meal not found'}, status=404)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def meals_for_date(request, date):
    try:
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return HttpResponseBadRequest("Invalid date format")

    meals = Meal.objects.filter(user=request.user, date=date_obj)

    total_calories = sum(meal.calories for meal in meals)
    total_protein = sum(meal.protein for meal in meals)
    total_carbohydrates = sum(meal.carbohydrates for meal in meals)
    total_fat = sum(meal.fat for meal in meals)
    calorie_goal = request.user.daily_calorie_goal
    remaining_calories = calorie_goal - total_calories if calorie_goal else None

    context = {
        'meals': meals,
        'selected_date': date,
        'total_calories': total_calories,
        'total_protein': total_protein,
        'total_carbohydrates': total_carbohydrates,
        'total_fat': total_fat,
        'remaining_calories': remaining_calories,
        'calorie_goal': calorie_goal,
    }

    return render(request, 'meals/meal_list.html', context)