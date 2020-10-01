import random
number=random.randrange(1,100)
guess=(int(input("Guess a number between 1 to 100:")))
while guess!=number:
    if guess<number:
        print("You need to guess a higher number.Try again!!")
        guess=(int(input("\n Guess a number between 1 and 100:")))
    else:
        print("You need to guess a lower number.Try again!!")
        guess=(int(input("\nGuess a lower number between 1 and 100:")))
print("You have guessed the number correctly!!")





