from flask import render_template, request, make_response, jsonify
from arrotechtools import Serializer

from app.api.v1 import blueprint_v1
from .models import Recipe
from app.extensions import db

# write your views here


@blueprint_v1.route('/recipes', methods=['POST'])
def add_recipe():
    """Home page endpoint."""

    details = request.get_json()
    title = details['title']
    ingredients = details['ingredients']
    steps = details['steps']

    recipe = Recipe(title=title, ingredients=ingredients, steps=steps)

    db.session.add(recipe)
    db.session.commit()

    return Serializer.serialize(recipe.as_dict(), 201, "Recipe added successfully")


@blueprint_v1.route('/recipes', methods=['GET'])
def get_all_recipes():
    """Get all recipes."""

    recipes = {
        "recipes": Recipe.query.all()
    }

    dict_recipes = []
    for recipe in recipes['recipes']:
        dict_recipes.append(recipe.as_dict())

    return Serializer.serialize(dict_recipes, 200, "Recipe retrieved successfully")


@blueprint_v1.route('/recipes/five', methods=['GET'])
def get_five_recipes():
    """Display the first five recipes."""

    recipes = {
        "recipes": Recipe.query.limit(5).all()
    }

    dict_recipes = []
    for recipe in recipes['recipes']:
        dict_recipes.append(recipe.as_dict())

    return Serializer.serialize(dict_recipes, 200, "Recipe retrieved successfully")


@blueprint_v1.route('/recipes/<int:id>', methods=['GET'])
def get_a_recipe(id):
    """Get a recipe by id."""

    recipe = Recipe.query.filter_by(id=id).first()
    if recipe:
        return Serializer.serialize(recipe.as_dict(), 200, "Recipe retrieved successfully")
    return Serializer.raise_error(404, "Recipe not found")


@blueprint_v1.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    """Update a recipe by id."""
    details = request.get_json()
    title = details['title']
    ingredients = details['ingredients']
    steps = details['steps']

    recipe = Recipe.query.filter_by(id=id).first()

    recipe.title = title
    recipe.ingredients = ingredients
    recipe.steps = steps

    db.session.commit()

    return Serializer.serialize(recipe.as_dict(), 200, "Recipe updated successfully")

@blueprint_v1.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    """Delete recipe by Id."""

    recipe = Recipe.query.filter_by(id=id).first()
    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        return Serializer.on_success(204, "Recipe deleted successfully")
    return Serializer.raise_error(404, "Recipe not found")
