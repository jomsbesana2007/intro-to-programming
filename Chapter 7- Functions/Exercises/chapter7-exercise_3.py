## Exercise 3: T-Shirt

# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 

# The function should print a sentence summarizing the size of the shirt and the message printed on it. 

# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.


# The make_shirt function that accepts size and text parameters to make a shirt
def make_shirt(size, text):
    print(f"The size of your shirt will be: {size}")
    print(f"The text printed on your shirt will be: {text}")

# The function call containing the size and text parameters
make_shirt("large", "Keep calm and Learn Python!")


# The function but without any parameters passed
def make_shirt(size, text):
    print(f"The size of your shirt will be: {size}")
    print(f"The text printed on your shirt will be: {text}")

make_shirt()