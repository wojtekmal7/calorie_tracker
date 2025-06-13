from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    activity_level = models.CharField(max_length=20, choices=[
        ('Sedentary', 'Sedentary'),
        ('Lightly active', 'Lightly active'),
        ('Moderately active', 'Moderately active'),
        ('Very active', 'Very active')
    ], null=True, blank=True)
    daily_calorie_goal = models.IntegerField(null=True, blank=True)
    target_weight = models.FloatField(null=True, blank=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.username

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.IntegerField(null=True, blank=True)
    carbohydrates = models.IntegerField(null=True, blank=True)
    fat = models.IntegerField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    meal = models.ForeignKey(Meal, related_name='ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)