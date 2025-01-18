## Exercise 3: Glossary 2 

# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

# calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

# to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

python_glossary = {
    'Variables': "Stores values, whether it is a string, float, or integer, for later use. The values inside variables can change, hence its name.",
    'Strings': "It is a data type that represents a series of characters.",
    'Lists': "Stores multiple values in one single list. They can be accessed by calling a value's index (e.g., name[0], name[1])",
    'Dictionaries': "They are used to store data values in key-value pairs (e.g., 'name': 'John').",
    'Integers': "It is a data type that represents zero, positive, or negative whole numbers.",
    'Floats': "It is a data type that represents numbers with one or more decimals.",
    'For Loop': "It goes through all values in either a list, a dictionary, a tuple, or a set.",
    'If-Else Statements': "They are statements that specify a condition by comparing two values and the result will determine the next course of action.",
    'Indentation': "A space in the beginning of a code line.",
    'While Loop': "It executes a set of statements or code as long as a condition stays true.",
}

# Loops through each key and their values
for key, value in python_glossary.items():
    print(f"{key}:\n{value}\n")