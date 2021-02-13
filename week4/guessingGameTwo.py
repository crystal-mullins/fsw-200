intro = "To win you must guess the secret number. It\'s a number between 1 and 9 (including 1 and 9). \nType exit whenever you want to quit." 
print(intro)
import random
number = random.randint(1, 9)
guess = 0
count = 0
while guess != number and guess != "exit":
    guess = input("\nWhat's your guess? ")
    if guess == "exit":
        print ("Quiters never win!")
        break
    guess = int(guess)
    count += 1
    if guess < number:
        print("That is too low!")
    elif guess > number:
        print("That is too high!")
    else:
        print("You got it!")
        print("It took you", count, "tries!")