import random

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid_move(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def fill_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid_move(grid, i, j, num):
                        grid[i][j] = num
                        if fill_grid(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def remove_cells(grid, difficulty):
    cells_to_remove = {"easy": 30, "medium": 40, "hard": 50}
    count = cells_to_remove.get(difficulty, 40)
    while count > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
            count -= 1

def generate_sudoku(difficulty="medium"):
    grid = [[0 for _ in range(9)] for _ in range(9)]
    fill_grid(grid)
    remove_cells(grid, difficulty)
    return grid

if __name__ == "__main__":
    while True:
        difficulty = input("Enter difficulty (easy, medium, hard, or exit to quit): ").lower()
        if difficulty == "exit":
            print("Exiting the program.")
            break
        elif difficulty in {"easy", "medium", "hard"}:
            sudoku = generate_sudoku(difficulty)
            print("Generated Sudoku:")
            print_grid(sudoku)
        else:
            print("Invalid input. Please enter 'easy', 'medium', 'hard', or 'exit'.")
