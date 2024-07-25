import random

dice_value_count = 0
dice_rolled_count = 0
print("----Dice Rolling Simulator----\n")
print("////Made by Harshit Oberoi////\n")

play = input("Do you want to roll a dice? (enter y): \n")

while play == "y":
	
	print("You rolled a dice")
	dice_value = random.randint(1, 6)
	print(f"Number on Dice: {dice_value}")	
	
	play = input("Would you like to continue?: ")


	dice_value_count += dice_value
	dice_rolled_count += 1

print(f"\nYour dice rolls add up to {dice_value_count}")
print(f"You rolled a dice {dice_rolled_count} times")


