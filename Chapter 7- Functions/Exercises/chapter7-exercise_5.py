## Exercise 5: Cities

# Write a function called describe_city() that accepts the name of a city and its country. 

# The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.

# Call your function for three different cities, at least one of which is not in the default country.


# The describe_city function that accepts the parameters 'city' and 'country'
def describe_city(city, country = "Germany"):
    print(f"{city} is in {country}")

# The function calls
describe_city("Frankurt am Main")

describe_city("Berlin")

describe_city("Budapest", "Hungary")