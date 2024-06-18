# Title: Coin Flip streak
# Author: Vinit Chawda
# Date: 14th June 2024

theboard = {"topl":' ',"topm":' ',"topr":' ',
            "midl":' ',"midm":' ',"midr":' ',
            "lowl":' ',"lowm":' ',"lowr":' '}

def printboard(theboard):
    print(theboard['topl'] + ' | ' + theboard['topm'] + ' | ' + theboard['topr'])
    print('--+---+--')
    print(theboard['midl'] + ' | ' + theboard['midm'] + ' | ' + theboard['midr'])
    print('--+---+--')
    print(theboard['lowl'] + ' | ' + theboard['lowm'] + ' | ' + theboard['lowr'])


def check_winner(board):

    # Rows
    if board['topl'] == board['topm'] == board['topr'] != ' ':
        return board['topl']
    if board['midl'] == board['midm'] == board['midr'] != ' ':
        return board['midl']
    if board['lowl'] == board['lowm'] == board['lowr'] != ' ':
        return board['lowl']

    # Columns
    if board['topl'] == board['midl'] == board['lowl'] != ' ':
        return board['topl']
    if board['topm'] == board['midm'] == board['lowm'] != ' ':
        return board['topm']
    if board['topr'] == board['midr'] == board['lowr'] != ' ':
        return board['topr']

    # Diagonals
    if board['topl'] == board['midm'] == board['lowr'] != ' ':
        return board['topl']

    if board['topr'] == board['midm'] == board['lowl'] != ' ':
        return board['topr']
    
    return None

    

turn = 'X'
winner = check_winner(theboard)
move_count = 0

while move_count < 9:
    printboard(theboard)
    move = input('Enter your move (e.g.topl,midm,lowr) :  ').lower()
    if move not in theboard or theboard[move] != ' ':
        print('Invalid move please try again.')
        continue
    theboard[move] = turn
    move_count += 1
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    winner = check_winner(theboard)
    if winner:
        print(f"Yayyyyy! The winner is {winner}")
        break

if not winner:
    printboard(theboard)
    print("It's a draw")