from flask import Flask, make_response, request
from flask_migrate import Migrate

from models import db, Recipe, RecipeIngredient, Ingredient

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# @app.route('/')
# def index():
#   response_body = <p>"Try the following routes:\n/recipes\n/recipe/<int:id>\n/ingredients\n/ingredient/<int:id>"<p>
#   return make_response(response_body, 200)


#recipes
@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
  if request.method == 'GET':
    recipes = Recipe.query.all()
    response_body = [recipe.to_dict() for recipe in recipes]
    return make_response(response_body, 200) #200 means ok
  
  elif request.method == 'POST':
    form_data = request.get_json()
    new_recipe = Recipe(title=form_data.get('title'), instructions=form_data.get('instructions'), servings=form_data.get('servings'))
    db.session.add(new_recipe)
    db.session.commit()
    return make_response(new_recipe.to_dict(), 201) #201 means ok/created

@app.route('/recipe/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def recipe_by_id(id):
  if request.method == 'GET':
    recipe = Recipe.query.filter_by(id = id).first()
    if recipe:
      response_body = recipe.to_dict()
      status_code = 200
    else:
      response_body = {"message": f"Recipe {recipe.id} not found"}
      status_code = 404
    return make_response(response_body, status_code)


#ingredients
@app.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
  if request.method == 'GET':
    ingredients = Ingredient.query.all()
    response_body = [ingredient.to_dict() for ingredient in ingredients]
    return make_response(response_body, 200)
  elif request.method == 'POST':
    form_data = request.get_json()
    new_ingredient = Ingredient(name=form_data.get('name'), type=form_data.get('type'))
    db.session.add(new_ingredient)
    db.session.commit()
    return make_response(new_ingredient.to_dict(), 201)

@app.route('/ingredient/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def ingredient(id):
  if request.method == 'GET':
    ingredient = Ingredient.query.filter_by(id=id).first()
    if ingredient:
      response_body = ingredient.to_dict()
      status_code = 200
    else:
      response_body = {"message": f"Ingredient {ingredient.id} not found"}
      status_code = 404
    return make_response(response_body, status_code)

if __name__ == '__main__':
  app.run(port=5555, debug=True)