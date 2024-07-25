print("----Text Based Adventure Game----\n")
print("----Made By Harshit Oberoi----\n")

print("Mission: Go on an adventure to find the way out of this maze.")
print("To start the game input 'start'")
print("To read the instrucions input 'manual'")

room_count = 0
start = input("Enter the command: ")

while True:
	if start == "start":
		print("\nThe game began!")
		print("You are in the starting room.")
		print("There are three doors in front of you.")
		print("Door 1 | Door 2 | Door 3")
		room = input("Which room do you want to enter?: ")
		
		if room == "1":
			print("\nYou entered a room.")
			print("There is a Door in front of you.")
			print("Door 1")
			room_count += 1
			room = input("Which room do you want to enter?: ")
			
			if room == "1":
				print("\nYou entered a room.")
				print("This is a closed room.")
				print("There are no more doors to enter.")
				print("You were unable to solve the maze.")
				room_count += 1
				break

		elif room == "2":
			print("\nYou enterd a room.")
			print("This is a closed room.")
			print("There are no more doors to enter.")
			print("You were unable to solve the maze.")
			room_count += 1
			break

		elif room == "3":
			print("\nYou entered a room.")
			print("There are two doors in front of you.")
			print("Door 1 | Door 2")
			room_count += 1
			room = input("Which room do you want to enter?: ")
			
			if room == "1":
				print("\nYou entered a room.")
				print("There is a open door in front of you.")
				print("Light is coming inside from outside the door.")
				print("You head towards the light.")
				print("You have found your way out of the maze of rooms.")
				print("Well Done!")
				room_count +=1
				break

			elif room == "2":
				print("\nYou enterd a room.")
				print("This is a closed room.")
				print("There are no more doors to enter.")
				print("You were unable to solve the maze.")
				room_count += 1
				break


	elif start == "manual":
		print("\nThis is an adventure game.")
		print("You are stuck in a maze of rooms.")
		print("When the game starts, your player will be in the starting room.")
		print("The next possible rooms to enter will be displayed.")
		print("To enter the desired room, input the room number.")
		print("For example: to enter room 2 from the given rooms input 2")
		print("When you enter a room that is closed, you will lose.")
		print("Good Luck!")
		start = input("\nEnter the command: ")

if room_count > 1:
	print("\nYou entered " + str((room_count)) + " rooms during your adventure.")

else:
	print(print("\nYou entered only one room during your adventure."))
