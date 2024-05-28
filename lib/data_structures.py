spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # Initializing an empty list to store the names of spicy foods
    names = []
    
    # Iterating over each spicy food dictionary
    for food in spicy_foods:
        # This will Extract the name of the spicy food and append it to the names list
        names.append(food["name"])
    
    #This  Return the list of names
    return names

def get_spiciest_foods(spicy_foods):
    # Initialize an empty list to store the spiciest foods
    spiciest_foods = []
    
    # Iterate over each spicy food dictionary
    for food in spicy_foods:
        # Check if the heat level of the food is greater than 5
        if food["heat_level"] > 5:
            # If so, add the food to the spiciest_foods list
            spiciest_foods.append(food)
    
    # Return the list of spiciest foods
    return spiciest_foods
def print_spicy_foods(spicy_foods):
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # This Iterates over each spicy food dictionary
    for food in spicy_foods:
        # Checks if the cuisine of the food matches the input cuisine
        if food["cuisine"] == cuisine:
            # return the food dictionary, If so,
            return food
    
    # If no matching food is found, return None
    return None

def print_spiciest_foods(spicy_foods):#Unable to do
    pass

def get_average_heat_level(spicy_foods):#Unable to do
    pass

def create_spicy_food(spicy_foods, spicy_food):
    # Appends the new spicy_food to the existing list of spicy_foods
    spicy_foods.append(spicy_food)
    
    # This Returns the updated list of spicy_foods
    return spicy_foods
