## Exercise 5: Pets 

# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. 

# Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet


# A list storing the dictionaries of different pets, owners, and their characteristics 
pets = [
    # John's pet dog
    {
        'animal_type': 'dog',
        'name_of_owner': 'John',
        'color': 'brown',
        'breed': 'German Shepherd',
    },

    # Maria's pet cat
    {
        'animal_type': 'cat',
        'name_of_owner': 'Maria',
        'color': 'white',
        'breed': 'Turkish Van',
    },

    # Lance's pet hamster
    {
        'animal_type': 'hamster',
        'name_of_owner': 'Lance',
        'color': 'white',
        'breed': 'Chinese Hamster',
    },

    # Josh's pet cat
    {
        'animal_type': 'cat',
        'name_of_owner': 'Josh',
        'color': 'black',
        'breed': 'American Shorthair',
    },

    # Philip's pet dog
    {
        'animal_type': 'dog',
        'name_of_owner': 'Philip',
        'color': 'white',
        'breed': 'Chihuahua',
    },
]

# Loops through the list
for pet in pets:
    print(f"{pet['name_of_owner']}'s pet is a {pet['animal_type']}\n"
          f"The pet's color is: {pet['color']}\n"
          f"The pet's breed is: {pet['breed']}\n")