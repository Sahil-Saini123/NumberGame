import random
import math
lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)
print("\n\tYou've only ",round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

while count < round(math.log(upper - lower + 1, 2)):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		break
	elif x > guess:
		print("You guessed a smaller number")
	elif x < guess:
		print("You Guessed a greater number")

if count == round(math.log(upper - lower + 1, 2)):
        if guess != x:
                print("\nThe number is",x)
                print("\tBetter Luck Next time!")
