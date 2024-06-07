import random

secret_number = random.randint(1,20)

print('Guess the number to win the game, where number lies between 1 to 20.')
print("You will have 6 chances to guess the number.")

# Ask the user to take a guess
for guessestaken in range(1,7):
    guess = int(input("Enter the number: "))

    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        break       #condition is correct

if guess == secret_number:
    print("Good job! You won the game by guessing correct number in " + str(guessestaken) + " guessess!")
else:
    print("Oops! you lost all your 6 chances and lost the game")