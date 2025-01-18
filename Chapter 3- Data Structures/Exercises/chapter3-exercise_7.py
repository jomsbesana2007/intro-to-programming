## Exercise 7: Seeing the World :ballot_box_with_check:
# Think of at least five places in the world you’d like to visit.

# •	 Store the locations in a list. Make sure the list is not in alphabetical order.
# •	 Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
# •	 Use sorted() to print your list in alphabetical order without modifying the actual list.
# •	 Show that your list is still in its original order by printing it.
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# •	 Show that your list is still in its original order by printing it again.
# •	 Use reverse() to change the order of your list. Print the list to show that its order has changed.
# •	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# •	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.


# The places I'd like to visit
desiredPlacesToVisit = ['Germany', 'Turkey', 'Hungary', 'Switzerland', 'Singapore']

# Prints the unsorted list
print(f"Unsorted list: {desiredPlacesToVisit}\n")

# Prints the sorted list and the original list
print(f"Sorted list: {sorted(desiredPlacesToVisit)}\n"
      f"Original list: {desiredPlacesToVisit}\n")

# Prints the sorted list in reverse and the original list
print(f"Reverse sorted list: {sorted(desiredPlacesToVisit, reverse= True)}\n"
      f"Original list: {desiredPlacesToVisit}\n")

# Prints out the original list that has been reversed using reverse() and vice versa
desiredPlacesToVisit.reverse()
print(f"Reversed original list: {desiredPlacesToVisit}")

desiredPlacesToVisit.reverse()
print(f"Reversed original list so that it is in its actual original order:{desiredPlacesToVisit}\n")

# Prints out the original list that has been alphabetically sorted and in reverse
desiredPlacesToVisit.sort()
print(f"Alphabetically sorted list: {desiredPlacesToVisit}")

desiredPlacesToVisit.sort(reverse= True)
print(f"Reversed alphabetically sorted list: {desiredPlacesToVisit}\n")

# Python sorted() function source: https://www.w3schools.com/python/ref_func_sorted.asp