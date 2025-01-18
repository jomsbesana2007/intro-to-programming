## Exercise 4: Rivers 

# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

# * Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# * Use a loop to print the name of each river included in the dictionary.
# * Use a loop to print the name of each country included in the dictionary.


# A dictionary containing all the major rivers and their respective countries
majorRivers = {
    'Missouri River': 'USA',
    'Amazon River': 'Brazil',
    'Yangtze River': 'China',
}

# A for loop going through all the key-value pairs in the major_rivers dictionary
for river, country in majorRivers.items():
    print(f"The {river} is the longest river in {country}.\n")