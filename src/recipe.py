from json import JSONEncoder


class Ingredient:
    def __init__(self, quantity=None, product=None, comment=None):
        self.quantity = quantity
        self.product = product
        self.comment = comment


class Recipe:
    def __init__(self):
        self.ingredients = []
        self.steps_of_cooking = []

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def add_step(self, step: str):
        self.steps_of_cooking.append(step)


class RecipeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
