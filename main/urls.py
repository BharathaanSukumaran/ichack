from django.urls import path
from . import views
from django.http import HttpRequest, HttpResponse


urlpatterns = [
    path('recipe',views.get_recipes,name='recipe'),
    path('',views.HomeView,name=''),
    path('recipe/<recipe>',views.RecipeView,name='product'),
    path('form',views.form_method,name='form'),

]