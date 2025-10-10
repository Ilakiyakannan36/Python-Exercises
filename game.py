# to guess a number and finding whether it is equal to the random number
import random

secret_number = random.randint(1, 20)
print("***Number Guess***")

while True:
        guess = int(input("Take a guess: "))

        if guess < secret_number:
                print("The guess is low... higher number... Try again.")
        elif guess > secret_number:
                print("The guess is higher... lower number...Try again.")
        else:
                print(f"Congratulations! You guessed it right. The number was {secret_number}.")
                break
