import json

from src.bbcgoodfood_parser import parse


def test_parser_recipe_1():
    json_recipe = parse('https://www.bbcgoodfood.com/recipes/meatball-black-bean-chilli')
    dict_recipe = json.loads(json_recipe)
    assert len(dict_recipe['ingredients']) == 12
    assert len(dict_recipe['steps_of_cooking']) == 3
    assert dict_recipe['ingredients'][0]['quantity'] == '2 tbsp'
    assert dict_recipe['ingredients'][0]['product'] == 'olive oil'


def test_parser_recipe_2():
    json_recipe = parse('https://www.bbcgoodfood.com/recipes/black-forest-arctic-roll')
    dict_recipe = json.loads(json_recipe)
    assert len(dict_recipe['ingredients']) == 14
    assert len(dict_recipe['steps_of_cooking']) == 5
    assert dict_recipe['ingredients'][0]['quantity'] == '2'
    assert dict_recipe['ingredients'][0]['product'] == 'eggs'
    assert dict_recipe['ingredients'][0]['comment'] == 'separated'


def test_parser_recipe_3():
    json_recipe = parse('https://www.bbcgoodfood.com/recipes/roasted-aubergine-tomato-curry')
    dict_recipe = json.loads(json_recipe)
    assert len(dict_recipe['ingredients']) == 12
    assert len(dict_recipe['steps_of_cooking']) == 3
    assert dict_recipe['ingredients'][0]['quantity'] == '600g'
    assert dict_recipe['ingredients'][0]['product'] == 'baby aubergines'
    assert dict_recipe['ingredients'][0]['comment'] == 'sliced into rounds'