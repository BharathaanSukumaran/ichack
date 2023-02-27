from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, BadHeaderError
import spoonacular as sp 
from tools import ichackWebScraper, data_handler
from .forms import ItemForm

# Create your views here.


query = sp.API("9a5ae06209ce4ec4acca1b540e52ddcd")
output = {}
def filter_dict_by_keys(d,keys = ['name','amount','unit']):
    return {k: v for k, v in d.items() if k in keys}

def get_ingredients(recipe):
    unused_ingredients = recipe["missedIngredients"]
    used_ingredients = recipe["usedIngredients"]
    ingredients_list = unused_ingredients+used_ingredients
    output_list = []
    for item in ingredients_list:
        output_list.append(filter_dict_by_keys(item))
        

    return output_list

def get_recipes(request):
    ingredients = ["orange"]
    response = query.search_recipes_by_ingredients(ingredients,number = 8, limitLicense = False, ranking = 2).json()
    for recipes in response:
        output[recipes['title']] = (get_ingredients(recipes),recipes["image"])
        output[recipes['title']][0].append(ichackWebScraper.search_google(recipes["title"]))


    return render(request,"recipe.html",{'output':output})

def HomeView(request):
    return render(request,"index.html") 

def RecipeView(request,recipe):
    recipe_dict = output[str(recipe)][0][:-1]
    image = output[str(recipe)][1]
    url = output[str(recipe)][0][-1]

    name = recipe.title()
    return render(request,"ProductViewImproved.html",{"recipe":recipe_dict,"name":name,"image":image, "url":url})  


def form_method(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            body = {
            'Item Ingredient': form.cleaned_data['ingredients'], 
            'Item Amount': form.cleaned_data['amount'], 
            'Item Unit': form.cleaned_data['units'], 
            'Item Expiration Date':form.cleaned_data['expiry_date'], 
            }

            if(BadHeaderError):
                return HttpResponse('Invalid header found.')
            return redirect ('form')
      
    form = ItemForm()
    return render(request, "form.html", {'form':form})