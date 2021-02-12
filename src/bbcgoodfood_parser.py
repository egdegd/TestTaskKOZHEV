import bs4
import requests
from bs4 import BeautifulSoup
import json
from src.recipe import *


def parse(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    recipe = Recipe()

    ingredients = parse_ingredients(soup)
    for ingredient in ingredients:
        recipe.add_ingredient(ingredient)

    steps_of_cooking = parse_method(soup)
    for step in steps_of_cooking:
        recipe.add_step(step)

    recipe_json_data = json.dumps(recipe, indent=4, cls=RecipeEncoder)
    return recipe_json_data


special_quantities = [188, 189, 190]  # ord(1/4), ord(1/2), ord(3/4)


def is_quantity(quantity):
    return any(map(lambda ch: str.isdigit(ch) or ord(ch) in special_quantities, quantity))


def delete_unnecessary_characters(string):
    bad_symbols = [',', ' ']
    flag = True
    while flag:
        flag = False
        if string[-1] in bad_symbols:
            string = string[:-1]
            flag = True
        if string[0] in bad_symbols:
            string = string[1:]
            flag = True
    return string


def parse_ingredients(soup):
    tags = soup.find_all(class_="pb-xxs pt-xxs list-item list-item--separator")
    ingredients = []
    for tag in tags:
        arg = []
        for child in tag.descendants:
            if type(child) == bs4.element.NavigableString:
                str_child = str(child)
                str_child = delete_unnecessary_characters(str_child)
                arg.append(str_child)
        new_ingredient = Ingredient()
        if is_quantity(arg[0]):
            new_ingredient.quantity = arg[0]
            new_ingredient.product = arg[1]
            if len(arg) == 3:
                new_ingredient.comment = arg[2]
        else:
            new_ingredient.product = arg[0]
            if len(arg) == 2:
                new_ingredient.comment = arg[1]
        ingredients.append(new_ingredient)
    return ingredients


def parse_method(soup):
    steps_of_cooking = []
    tags = soup.find_all(class_="pb-xs pt-xs list-item")
    for tag in tags:
        steps_of_cooking.append(tag.find_all(class_="editor-content")[0].text)
    return steps_of_cooking


# recipe = parse('https://www.bbcgoodfood.com/recipes/meatball-black-bean-chilli')
# print(recipe)
