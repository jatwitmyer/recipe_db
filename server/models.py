from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(
  naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  }
)

db = SQLAlchemy(metadata=metadata)

# Users >< Recipes
# Recipes >< Ingredients


class Recipe(db.Model, SerializerMixin):
  __tablename__ = 'recipes'

  serialize_rules = ('-recipes_ingredients.recipe', )

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  instructions = db.Column(db.String)
  servings = db.Column(db.Integer)

  recipes_ingredients = db.relationship('RecipeIngredient', back_populates='recipe', cascade='all, delete-orphan')

  ingredients = association_proxy('recipes_ingredients', 'ingredient')

  def __repr__(self):
    return f'<Recipe {self.id}: {self.title}, Servings: {self.servings}, Instructions: {self.instructions}>'
  

class Ingredient(db.Model, SerializerMixin):
  __tablename__ = 'ingredients'

  serialize_rules = ('-recipes_ingredients.ingredient', )

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  type = db.Column(db.String)

  recipes_ingredients = db.relationship('RecipeIngredient', back_populates='ingredient', cascade='all, delete-orphan')

  recipes = association_proxy('recipes_ingredients', 'recipe')

  def __repr__(self):
    if self.type:
      return f'<Ingredient {self.id}: {self.type} {self.name}>'
    else:
      return f'<Ingredient {self.id}: {self.name}>'


class RecipeIngredient(db.Model, SerializerMixin):
  __tablename__ = 'recipes_ingredients'

  serialize_rules = ('-recipe.recipes_ingredients', '-recipe.ingredients', '-ingredient.recipes_ingredients', '-ingredient.recipes')

  id = db.Column(db.Integer, primary_key=True)
  quantity = db.Column(db.Integer)
  unit_of_measure = db.Column(db.String)
  processed = db.Column(db.String)

  recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
  ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'))

  recipe = db.relationship('Recipe', back_populates='recipes_ingredients')
  ingredient = db.relationship('Ingredient', back_populates='recipes_ingredients')

  def __repr__(self):
    if self.processed:
      return f'<ID {self.id}: {self.quantity} {self.unit_of_measure} of {self.ingredient.name}, {self.processed}>'
    else:
      return f'<ID {self.id}: {self.quantity} {self.unit_of_measure} of {self.ingredient.name}>'