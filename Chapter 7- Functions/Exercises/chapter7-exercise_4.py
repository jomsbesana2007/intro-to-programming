## Exercise 4:  Large Shirts

# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 

# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.


# The make_shirt function with "Large" as the default size and "I love Python!" as the default text
def make_shirt(size="Large", text="I love Python!"):
    print(f"The size of your shirt will be: {size}")
    print(f"The text printed on your shirt will be: {text}\n")

# The function calls
make_shirt()

make_shirt("Medium")

make_shirt("Extra large", "Deck the halls with boughs of holly!")