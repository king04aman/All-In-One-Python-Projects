import requests
import random

# Replace 'your_api_key_here' with your actual Spoonacular API key
API_KEY = "74de4b7826b74b70b4d3a0fe3191239a"
BASE_URL = "https://api.spoonacular.com/recipes"

def find_recipes(ingredients):
    """Search for recipes based on ingredients using the Spoonacular API."""
    url = f"{BASE_URL}/findByIngredients"
    params = {
        'ingredients': ','.join(ingredients),
        'number': 10,  # Get up to 10 recipes
        'apiKey': API_KEY
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        recipes = response.json()
        return [(recipe['title'], recipe['id']) for recipe in recipes]
    else:
        print(f"Error: {response.status_code}")
        return []

def get_recipe_details(recipe_id):
    """Get details of a specific recipe by its ID."""
    url = f"{BASE_URL}/{recipe_id}/information"
    params = {'apiKey': API_KEY}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def plan_meals(ingredients):
    """Plan meals for the week based on available ingredients."""
    recipes = find_recipes(ingredients)
    
    if not recipes:
        return "No recipes found with the given ingredients."

    meals = random.sample(recipes, min(7, len(recipes)))
    return meals

def user_interface():
    print("Welcome to the Meal Planner!")
    print("Enter the ingredients you have, separated by commas:")
    
    ingredients = input().split(",")
    ingredients = [ingredient.strip().lower() for ingredient in ingredients]

    print("\nSearching for recipes based on your ingredients...\n")
    recipes = find_recipes(ingredients)

    if recipes:
        print(f"Found the following recipes with your ingredients:")
        for i, (title, _) in enumerate(recipes):
            print(f"{i + 1}. {title}")
    else:
        print("No recipes found with the given ingredients.")

    print("\nDo you want to plan meals for the week with these ingredients? (yes/no)")
    if input().strip().lower() == "yes":
        meals = plan_meals(ingredients)
        print("\nHere is your meal plan for the week:")
        for i, (title, recipe_id) in enumerate(meals, 1):
            print(f"Day {i}: {title}")
            recipe_details = get_recipe_details(recipe_id)
            if recipe_details:
                print(f"  - Ready in: {recipe_details['readyInMinutes']} minutes")
                print(f"  - Servings: {recipe_details['servings']}")
    else:
        print("No meal plan generated.")

if __name__ == "__main__":
    user_interface()
