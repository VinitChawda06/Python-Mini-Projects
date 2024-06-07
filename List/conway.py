# Title: Conway Game of Life
# Author: Vinit Chawda
# Date: 2nd June 2024

import time, random, copy

height = 20
width = 60 

nextcells = []

for x in range(width):
    column = [] # Creating a new column
    for y in range(height):
        if random.randint(0,1) == 0:
            column.append('#') # Adding a livinig cell
        else:
            column.append(' ') # Adding a dead cell
    nextcells.append(column) #nextcellls is a list of column list

while True:
    print('\n\n\n\n\n') # separate each step with newlines
    currentcells = copy.deepcopy(nextcells)

    # Print Current cells on the screen
    for y in range(height):
        for x in range(width):
            print(currentcells[x][y], end='')
        print()

    # Calculate the next step's cells based on current step's cells:
    for x in range(width):
        for y in range(height):
        # Get neighboring coordinates:
        # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height
            # Count number of living neighbors:
            numNeighbors = 0
            if currentcells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentcells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentcells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentcells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentcells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentcells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentcells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentcells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.
            # Set cell based on Conway's Game of Life rules:
            if currentcells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextcells[x][y] = '#'
            elif currentcells[x][y] == ' ' and numNeighbors == 3:
            # Dead cells with 3 neighbors become alive:
                nextcells[x][y] = '#'
            else:
            # Everything else dies or stays dead:
                nextcells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.