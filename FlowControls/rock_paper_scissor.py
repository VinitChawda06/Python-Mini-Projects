import random, sys

print("Rock, Paper, Scissor")
wins = 0
losses = 0
ties = 0

while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    while True:
        print('Enter your move: (r)ock , (p)aper , (s)cissor or (q)uit')
        move = input()
        if move == "q":
            sys.exit()
        if move == "r" or move == "p" or move == "s":
            break
        print("Type r ,p ,s to continue playing or q to Quit the game.")

    if move == 'r':
        print("Rock versus ...")
    elif move == 'p':
        print("Paper versus ...")
    elif move == 's':
        print("Scissor versus ...")

    randomgame = random.randint(1,3)
    if randomgame == 1:
        cmove = "r"
        print("Rock")
    elif randomgame == 2:
        cmove = "p"
        print("Paper")
    elif randomgame == 3:
        cmove = "s"
        print("Scissor")

    if move == cmove:
        print("It is a tie")
        ties += 1

    if move == 'r' and cmove == 'p':
        print("You lose!")
        losses += 1
    elif move == 'r' and cmove == 's':
        print("You Win!")
        wins += 1
    if move == 'p' and cmove == 's':
        print("You lose!")
        losses += 1
    elif move == 'p' and cmove == 'r':
        print("You Win!")
        wins += 1   
    if move == 's' and cmove == 'r':
        print("You lose!")
        losses += 1
    elif move == 's' and cmove == 'p':
        print("You Win!")
        wins += 1

    