import logic

def initialize_grid():
    matrix = [[0] * 4 for _ in range(4)]
    count = 0
    while count < 2:
        row, col = logic.generate_pos()
        num = logic.generate_tile_val()
        if matrix[row][col] == 0:
            matrix[row][col] = num
            count += 1
    
    return matrix
    
grid = initialize_grid()

def main(grid):
    game_over = False
    while not game_over:
        logic.print_grid(grid)
        key_input = input("Move (w/a/s/d): ")
        
        move_result = logic.move(key_input, grid)
        if move_result == 2048:
            print("Congratulations! You've reached 2048!")
            break
        elif move_result == True:
            game_over = True

    print("Game Over")
        

if __name__ == "__main__":
    main(grid)