## Exercise 1: Pizza Toppings

# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

# print a message saying you’ll add that topping to their pizza.


# The keep_going variable is initialised with the string value 'y'
keep_going = 'y'

# A while loop that prompts the user to add any toppings they'd like as much as they want until they break the loop
while keep_going == 'y':
    user_input = input("Type in which topping you would like in your pizza.\nIf you wish to not add anything else, type in 'quit': ")

    if user_input == 'quit':
        break

    print(f"\nOkay! We will add {user_input} to your pizza!\n")