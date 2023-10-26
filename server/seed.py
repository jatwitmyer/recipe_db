from app import app
from models import db, Recipe, RecipeIngredient, Ingredient

with app.app_context():

  Recipe.query.delete()
  RecipeIngredient.query.delete()
  Ingredient.query.delete()
  

  ### RECIPES ###
  r1 = Recipe(title="Baked Ziti", instructions="1. Chop onion and garlic; 2. Measure spices: 1 tsp rosemary, 1 tsp thyme, 1 tsp basil, 1 tsp oregano; 3. Heat a heavy pot to medium high; 4. Saute ground beef until half is brown. 5. Add onion, garlic, and spices to the pan. Saute until onions are translucent. 6. Pour in 3 jars of tomato sauce and 1 cup of bone broth; 7. Bring to a boil while stirring; 8. reduce heat to medium low, add a lid ajar, and simmer for 30 minutes, stirring at least every 10 minutes; 9. Bring a pot of water to boil; 10. Cook 12oz of pasta to package instructions; 11. Add a cup of pasta water to your sauce; 12. Drain pasta and combine with sauce; 13. Preheat oven to 350F; 14. Layer sauce, parmesan, and mozzarella in a casserole dish; 15. Tent dish with aluminum foil; 16. Bake for 40 minutes. Remove foil after 20 minutes; 17. Remove from oven and rest for 10 minutes", servings=8)
  # r2 = Recipe(title="", instructions="")
  recipes = [r1]
  db.session.add_all(recipes)
  db.session.commit()
  

  ### INGREDIENTS ###
  #dairy
  id1 = Ingredient(name="mozzarella")
  id2 = Ingredient(name="parmesan")

  #aromatics
  ia1 = Ingredient(name="garlic")
  ia2 = Ingredient(name="onion", type="large, white")
  ia3 = Ingredient(name="rosemary", type="dried")
  ia4 = Ingredient(name="thyme", type="dried")
  ia5 = Ingredient(name="basil", type="dried")
  ia6 = Ingredient(name="oregano", type="dried")
  ia7 = Ingredient(name="marinara", type="jarred")
  ia8 = Ingredient(name="bone broth")

  #fats
  if1 = Ingredient(name="olive oil")

  #proteins
  ip1 = Ingredient(name="ground beef")

  #grains
  ig1 = Ingredient(name="penne", type="dried")

  ingredients = [id1, id2, ia1, ia2, ia3, ia4, ia5, ia6, ia7, ia8, if1, ip1, ig1]
  db.session.add_all(ingredients)
  db.session.commit()


  ### RELATIONSHIPS ###
  # baked ziti
  bz1 = RecipeIngredient(recipe_id=r1.id, ingredient_id=id1.id, quantity=16, unit_of_measure="oz", processed="shredded")
  bz2 = RecipeIngredient(recipe_id=r1.id, ingredient_id=id2.id, quantity=8, unit_of_measure="oz", processed="shredded")
  bz3 = RecipeIngredient(recipe_id=r1.id, ingredient_id=ia1.id, quantity=5, unit_of_measure= "cloves", processed="diced")
  bz4 = RecipeIngredient(recipe_id=r1.id, ingredient_id=ia2.id, quantity=1, unit_of_measure="bulb", processed="diced", )
  bz5 = RecipeIngredient(recipe_id=r1.id, ingredient_id=ia3.id, quantity=1, unit_of_measure="tsp")
  bz6 = RecipeIngredient(recipe_id=r1.id, ingredient_id=ia4.id, quantity=1, unit_of_measure="tsp")
  bz7 = RecipeIngredient(recipe_id=r1.id, ingredient_id=ia5.id, quantity=1, unit_of_measure="tsp")
  bz8 = RecipeIngredient(recipe_id=r1.id, ingredient_id=ia6.id, quantity=1, unit_of_measure="tsp")
  bz9 = RecipeIngredient(recipe_id=r1.id, ingredient_id=ia7.id, quantity=24, unit_of_measure="oz")
  bz10 = RecipeIngredient(recipe_id=r1.id, ingredient_id=ia8.id, quantity=1, unit_of_measure="cup")
  bz11 = RecipeIngredient(recipe_id=r1.id, ingredient_id=if1.id, quantity=2, unit_of_measure="tbsp")
  bz12 = RecipeIngredient(recipe_id=r1.id, ingredient_id=ip1.id, quantity=1, unit_of_measure="lb")
  bz13 = RecipeIngredient(recipe_id=r1.id, ingredient_id=ig1.id, quantity=10, unit_of_measure="oz")

  recipes_ingredients = [bz1, bz2, bz3, bz4, bz5, bz6, bz7, bz8, bz9, bz10, bz11, bz12, bz13]
  db.session.add_all(recipes_ingredients)
  db.session.commit()