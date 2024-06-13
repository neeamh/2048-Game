import math as mt
import random as rnd

def generate_tile_val():
    return rnd.choice([2,4])

def generate_pos():
    row = rnd.randrange(0, 4)
    col = rnd.randrange(0, 4)
    return row, col

def generate_tile(grid):
    num = generate_tile_val()
    not_found = True
    while not_found:
        row, col = generate_pos()
        if grid[row][col] == 0:  # Correct condition to place a tile in an empty spot
            grid[row][col] = num
            not_found = False

    return num

def print_grid(grid):
    for i in range(len(grid)):
        print(grid[i])

def transpose(grid):
    return [list(row) for row in zip(*grid)]

def reverse(grid):
    return [row[::-1] for row in grid]

def any_moves_left(grid):
    # Check for any zeros in the grid (empty spaces)
    if any(0 in row for row in grid):
        return True
    
    # Check for possible merges horizontally
    for row in grid:
        for i in range(3):
            if row[i] == row[i + 1]:
                return True
    
    # Check for possible merges vertically
    transposed_grid = transpose(grid)
    for row in transposed_grid:
        for i in range(3):
            if row[i] == row[i + 1]:
                return True
    
    return False

def move_left(grid):
    for i in range(4):
        # Step 1: Remove all zeros and shift tiles to the left
        new_row = [num for num in grid[i] if num != 0]

        # Step 2: Merge tiles with the same value
        for j in range(len(new_row) - 1):
            if new_row[j] == new_row[j + 1]:
                new_row[j] *= 2
                new_row[j + 1] = 0

        # Step 3: Remove all zeros again after merging
        new_row = [num for num in new_row if num != 0]

        # Step 4: Add zeros to the end to maintain the grid size
        new_row.extend([0] * (4 - len(new_row)))

        # Step 5: Update the grid row
        grid[i] = new_row

def move_right(grid):
    reversed_grid = reverse(grid)
    move_left(reversed_grid)
    grid[:] = reverse(reversed_grid)

def move_up(grid):
    transposed_grid = transpose(grid)
    move_left(transposed_grid)
    grid[:] = transpose(transposed_grid)

def move_down(grid):
    transposed_grid = transpose(grid)
    move_right(transposed_grid)
    grid[:] = transpose(transposed_grid)

def move(input, grid):
    if input.lower() == 'a':  # Move left
        move_left(grid)
    elif input.lower() == 'd':  # Move right
        move_right(grid)
    elif input.lower() == 'w':  # Move up
        move_up(grid)
    elif input.lower() == 's':  # Move down
        move_down(grid)
        
    # Check for winning condition
    if any(2048 in row for row in grid):
        return 2048

    # Check if we should generate a new tile
    if any(0 in row for row in grid):
        generate_tile(grid)
    
    # Check if there are any moves left
    if not any_moves_left(grid):
        return True
    
    return False




    
    




    

    
    
    
    




