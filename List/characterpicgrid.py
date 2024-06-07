# Title: Character Picture grid
# Author: Vinit Chawda
# Date: 6th June 2024

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

number_of_rows = len(grid) # 9
number_of_columns = len(grid[0]) # 6

for columns in range(number_of_columns):
    for rows in range(number_of_rows):
        print(grid[rows][columns], end="")
    print()


