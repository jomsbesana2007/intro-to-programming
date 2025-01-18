## Exercise 5: Change Guest List

# You just heard that one of your guests can’t make it to dinner, 
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

# • Start with your program from Exercise 3-4. Add a print() call at the end of your program stating 
#   the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.


# The program from exercise no. 4
invitedPeople = ['Shostakovich', 'Mahler', 'Sibelius', 'Beethoven', 'Saint-Saëns']

for person in invitedPeople:
    print(f"Dear {person},\n\nYou are invited to the dinner to have a evening filled with joy and camaraderie.\n")

# Prints out the person not coming to dinner
print(f"Unfortunately, {invitedPeople[2]} is not able to come to dinner.\n")

# A new list
invitedPeople = ['Shostakovich', 'Mahler', 'Dvořák', 'Beethoven', 'Saint-Saëns']

# Prints out the new set of invitations 
for person in invitedPeople:
    print(f"Dear {person},\n\nYou are invited to the dinner to have a evening filled with joy and camaraderie.\n")