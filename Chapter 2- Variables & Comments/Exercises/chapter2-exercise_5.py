## Exercise 5: USB Shopper :ballot_box_with_check:

# A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

# You will to use the arithmetic operators to complete this exercise.


oneUsbStickCost = 6 # cost of one usb stick
initialBalance = 50 # the girl's total initial balance

totalNumberOfUSBSticks = int(initialBalance / oneUsbStickCost) # computes the number of usb sticks the girl can buy with the money she has

totalCostOfUSBSticks = int(totalNumberOfUSBSticks * oneUsbStickCost) # computes the total cost of those usb sticks she can buy with the money she has

remainingBalance = int(initialBalance % oneUsbStickCost) # the remaining change

print(f"\nWith £{initialBalance}, she can buy {totalNumberOfUSBSticks} USB sticks, costing £{totalCostOfUSBSticks} in total\n")
print(f"Her remaining spare change is £{remainingBalance}\n")

