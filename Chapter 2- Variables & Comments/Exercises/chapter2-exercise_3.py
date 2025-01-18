## Exercise 3: Stripping Names :ballot_box_with_check:

# Tidy up the code to make it easier to understand
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, “\t” and “\n”, at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
# Assign a name with whitespace characters at the beginning and end, including \t and \n


# Name with whitespaces around it
name_with_whitespace = "\n\n\tJean Sibelius\t\n"

# Name with whitespaces printed
print("Name with whitespace characters shown:", repr(name_with_whitespace))
      
print("\nName with whitespaces shown:", name_with_whitespace)

# Name with left-side whitespaces stripped
print("Name with left-side whitespaces stripped:", repr(name_with_whitespace.lstrip()))

# Name with right-side whitespaces stripped
print("Name with right-side whitespaces stripped:", repr(name_with_whitespace.rstrip()))

# Name with all whitespaces stripped
print("Name with all whitespaces stripped:", repr(name_with_whitespace.strip()))

# str() vs repr() in Python source: https://www.geeksforgeeks.org/str-vs-repr-in-python/
