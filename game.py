import random

secret_number=random.randint(1,20)
print(" Guess the number ")
while True:
    guess = int(input("Guessed value="))
    if guess < secret_number:
        print("The value is low")
        print("Try again")
    elif guess >secret_number:
        print("The value is high")
        print("Try again")
        
    else :
        print("You got it")
        print("Correct answer")
        break
