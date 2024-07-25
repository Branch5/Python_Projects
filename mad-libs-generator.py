import random

print("----Mad Libs Generator----\n")
print("----Made By Harshit Oberoi----\n")


adjective_count = 0
adjective_list = []
print("Enter a total of 5 adjectives.\n")

while adjective_count < 5:
	adjective = input("Enter an adjective: ")
	adjective_list.append(adjective)

	adjective_count += 1

noun_count = 0
noun_list = []
print("\nEnter a total of 6 nouns.\n")

while noun_count < 6:
	noun = input("Enter a noun: ")
	noun_list.append(noun)

	noun_count += 1


random.shuffle(adjective_list)
random.shuffle(noun_list)


print("\nHere is the mad libs generated using the values you input: (randomly assigned)\n")

print("The Ancient Tale:\n")

print("There lives a" ,adjective_list[0] ,noun_list[0], "in the")
print(noun_list[1], " near the " ,adjective_list[1] ,noun_list[2], ". It is a very")
print(adjective_list[2], "place famous for" ,noun_list[3],"and" ,noun_list[4])
print(", but is now not mentioned at all\n due to its" ,adjective_list[3], "nature.")
print("This can only be changed by the" ,adjective_list[4] ,noun_list[5])