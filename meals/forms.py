from django import forms
from .models import Meal
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'calories', 'protein', 'carbohydrates', 'fat']
        widgets = {
            'calories': forms.NumberInput(attrs={'min': 0, 'id': 'id_calories'}),
            'protein': forms.NumberInput(attrs={'min': 0, 'id': 'id_protein'}),
            'carbohydrates': forms.NumberInput(attrs={'min': 0, 'id': 'id_carbohydrates'}),
            'fat': forms.NumberInput(attrs={'min': 0, 'id': 'id_fat'}),
        }

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'date_of_birth', 'gender', 'height', 'weight', 'activity_level', 'daily_calorie_goal', 'target_weight']
