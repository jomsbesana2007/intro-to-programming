## Exercise 2: Glossary 

# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# * Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 

# their meanings as values.

# * Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 

# the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 

# each word-meaning pair in your output.


# A dictionary storing all the keys and their respective values
python_glossary = {
    'Variables': "Stores values, whether it is a string, float, or integer, for later use. The values inside variables can change, hence its name.",
    'Strings': "It is a data type that represents a series of characters.",
    'Lists': "Stores multiple values in one single list. They can be accessed by calling a value's index (e.g., name[0], name[1])",
    'Dictionaries': "They are used to store data values in key-value pairs (e.g., 'name': 'John').",
    'Integers': "It is a data type that represents zero, positive, or negative whole numbers.",
}

# Prints the terms in Python and their definitions
print(f"Variables:\n{python_glossary['Variables']}\n\n")
print(f"Strings:\n{python_glossary['Strings']}\n\n")
print(f"Lists:\n{python_glossary['Lists']}\n\n")
print(f"Dictionaries:\n{python_glossary['Dictionaries']}\n\n")
print(f"Integers:\n{python_glossary['Integers']}\n")