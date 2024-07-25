import random

print("----Hangman Game----\n")
print("----Made By Harshit Oberoi----\n")

print("Guess the correct word.")

wordlist = ['hello', 'world', 'this', 'is', 'harry']

random.shuffle(wordlist)

word = list(wordlist[0])

display = []

display.extend(word)

for i in range(len(display)):
	display[i] = '_'

print(' '.join(display))
print()

count = 0

while count < len(word):
	guess = input("Guess a letter: ")
	guess = guess.lower()
	

	for i in range(len(word)):
		if word[i] == guess:
			display[i] = guess
			count += 1
			print(count)

			
print(' '.join(display))
print()


print("Well Done! You guessed the word.")