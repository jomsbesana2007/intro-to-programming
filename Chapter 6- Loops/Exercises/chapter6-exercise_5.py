## Exercise 5: No Pastrami

# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

# near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 

# occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.


sandwich_orders = ['Grilled cheese', 'Chicken sandwich', 'Pastrami', 
                   'Bánh mì', 'Pastrami', 'Croque monsieur', 'Pastrami', 'Pastrami']

finished_sandwiches = []

# Prints the message that the deli has run out of Pastrami sandwiches
print("\nThe deli has run out of Pastrami!\n")

# A while loop that removes each instance of 'Pastrami'
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

for sandwich in sandwich_orders:
    print(f"Your {sandwich} is done! Enjoy your meal!")
    finished_sandwiches.append(sandwich)

print(f"\nList of complete orders:\n{finished_sandwiches}\n")
    