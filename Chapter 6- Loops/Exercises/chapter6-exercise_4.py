## Exercise 4: Deli

# Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 

# move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.


# A list of the sandwich orders
sandwichOrders = ['Grilled cheese', 'Chicken sandwich', 'BLT sandwich', 
                   'Bánh mì', 'Chicken sandwich', 'Croque monsieur', 'Grilled cheese']

# An empty list of sandwich orders that are completed
finishedSandwiches = []

# A for loop that goes through each sandwich in the sandwich_orders list 
for sandwich in sandwichOrders:
    print(f"Your {sandwich} is done! Enjoy your meal!")
    finishedSandwiches.append(sandwich)
    
print(f"\nList of complete orders:\n{finishedSandwiches}\n")
