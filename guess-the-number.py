import random

print("----Guess The Number----\n")
print("----Made By Harshit Oberoi----\n")

random_number = random.randint(1, 9)

play = input("Do you want to play guess the number? (Enter y):")

if play == 'y':
	guess = int(input("Guess the random number: "))
	if guess == random_number:
		print("Well Done!")

	else:
		while guess != random_number:
			print("Try Agian")
			if guess > random_number:
				print("Guess Lower")

			elif guess < random_number:
				print("Guess Higher")

			guess = int(input("Guess the right number: "))
			if guess == random_number:
				print("You finally got it!")

else:
	print("\nGoodbye!")
