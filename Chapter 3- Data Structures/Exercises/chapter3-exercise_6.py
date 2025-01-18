## Exercise 6: Shrinking Guest List

# You just found out that your new dinner table won’t arrive in time for the dinner, 
# and you have space for only two guests.

# • Start with your program from Exercise 3-5. 
#   Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. 
#   Each time you pop a name from your list, print a message to that person letting them know you’re sorry 
#   you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. 
#   Print your list to make sure you actually have an empty list at the end of your program.


# The program from exercise no. 5
invitedPeople = ['Shostakovich', 'Mahler', 'Dvořák', 'Beethoven', 'Saint-Saëns']

for person in invitedPeople:
    print(f"Dear {person},\n\nYou are invited to the dinner to have a evening filled with joy and camaraderie.\n")

# Prints out the message that only 2 guests can come for dinner because the new dinner table won't arrive on time
print("Unfortunately, due to unforeseen circumstances, I am able to invite only two guests to dinner.\n")

# Prints out the apology message to each person as the pop() function remove each person from the list
for i in range(3):
    print(f"Dear {invitedPeople.pop()},\n\nSorry to hear that you won't be able to join the dinner tonight. I hope to see you soon!\n")

# Prints out to the remaining people still invited, informing them that they are still invited to dinner
for person in invitedPeople:
    print(f"Dear {person},\n\nYou are invited to the dinner to have a evening filled with joy and camaraderie.\n")

# The names of the remaining guests are wiped from the list
invited_people = []

# Prints out the empty list
print(invited_people)