# Title: Coin Flip streak
# Author: Vinit Chawda
# Date: 14th June 2024




def isValidChessboard(dictionary):
    valid_spaces = {num + character for num in '12345678' for character in 'abcdefgh'}
    
    white_king = 0
    black_king = 0
    white_pieces = 0
    black_pieces = 0
    white_pawn = 0
    black_pawn = 0

    for i,j in dictionary.items():
        if i not in valid_spaces:
            return False
        
        if 'w' in j[0]:
            white_pieces += 1
            if j == 'wking':
                white_king += 1
            
            if j == 'wpawn':
                white_pawn += 1
                  
        elif 'b' in j[0]:
            black_pieces += 1
            if j == 'bking':
                black_king += 1
            if j == 'bpawn':
                black_pawn += 1 

    print('White_pieces', white_pieces)
    print('White_Pawn', white_pawn)
    print('White_King', white_king)
    print('Black_pieces', black_pieces)
    print('Black_Pawn', black_pawn)
    print('Black_king', black_king)
    if white_king != 1:
        return False
    if white_pawn > 8:
        return False
    if white_pieces > 16:
        return False
        
    

    if black_king != 1:
        return False
    if black_pawn > 8:
        return False
    if black_pieces > 16:
        return False
    
    return True


chess_board_valid = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', 
    '5h': 'bqueen', '3e': 'wking', '2a': 'wrook', 
    '7f': 'bpawn', '8a': 'brook', '3a': 'wpawn', 
    '4d': 'wbishop', '6e': 'wknight', '5c': 'bknight', 
    '7d': 'bqueen', '8h': 'wrook', '4a': 'wpawn', 
    '3h': 'wpawn', '6h': 'bpawn', '7a': 'bpawn'
}

chess_board_too_many_pieces = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', 
    '5h': 'bqueen', '3e': 'wking', '2a': 'wrook', 
    '7f': 'bpawn', '8a': 'brook', '3a': 'wpawn', 
    '4d': 'wbishop', '6e': 'wknight', '5c': 'bknight', 
    '7d': 'bqueen', '8h': 'wrook', '4a': 'wpawn', 
    '3h': 'wpawn', '6h': 'bpawn', '7a': 'bpawn', 
    '8b': 'wqueen', '2b': 'wqueen', '5b': 'wknight'  # 17 pieces for white
}


chess_board_invalid_position = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', 
    '5h': 'bqueen', '3e': 'wking', '9a': 'wrook',  # Invalid position '9a'
    '7f': 'bpawn', '8a': 'brook', '3a': 'wpawn', 
    '4d': 'wbishop', '6e': 'wknight', '5c': 'bknight', 
    '7d': 'bqueen', '8h': 'wrook', '4a': 'wpawn', 
    '3h': 'wpawn', '6h': 'bpawn', '7a': 'bpawn'
}

chess_board_too_many_pawns = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', 
    '5h': 'bqueen', '3e': 'wking', '2a': 'wrook', 
    '7f': 'bpawn', '8a': 'brook', '3a': 'wpawn', 
    '4d': 'wbishop', '6e': 'wknight', '5c': 'bknight', 
    '7d': 'bqueen', '8h': 'wrook', '4a': 'wpawn', 
    '3h': 'wpawn', '6h': 'bpawn', '7a': 'bpawn', 
    '8f': 'bpawn', '5g': 'bpawn', '2h': 'bpawn'  # More than 8 pawns
}

chess_board_missing_white_king = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', 
    '5h': 'bqueen', '2a': 'wrook', '7f': 'bpawn', 
    '8a': 'brook', '3a': 'wpawn', '4d': 'wbishop', 
    '6e': 'wknight', '5c': 'bknight', '7d': 'bqueen', 
    '8h': 'wrook', '4a': 'wpawn', '3h': 'wpawn', 
    '6h': 'bpawn', '7a': 'bpawn'
}

   

# print(isValidChessboard(chess_board_valid))                  # Expected: True
# print(isValidChessboard(chess_board_too_many_pieces))        # Expected: False
# print(isValidChessboard(chess_board_invalid_position))       # Expected: False
# print(isValidChessboard(chess_board_too_many_pawns))         # Expected: False
print(isValidChessboard(chess_board_missing_white_king))     # Expected: False
