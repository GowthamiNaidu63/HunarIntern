def display_Path_to_Princess(N, grid):
    # Find the bot and princess positions
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'm':
                bot_pos = (i, j)
            elif grid[i][j] == 'p':
                princess_pos = (i, j)
    
    row_diff = princess_pos[0] - bot_pos[0]
    col_diff = princess_pos[1] - bot_pos[1]

    # Move in the direction of the row
    if row_diff < 0:
        for _ in range(abs(row_diff)):
            print("UP")
    elif row_diff > 0:
        for _ in range(row_diff):
            print("DOWN")

    # Move in the direction of the column
    if col_diff < 0:
        for _ in range(abs(col_diff)):
            print("LEFT")
    elif col_diff > 0:
        for _ in range(col_diff):
            print("RIGHT")


# Input section
N = int(input("Enter the number of rows (odd integer >= 3): "))
if N < 3 or N % 2 == 0:
    print("N must be an odd integer >= 3")
else:
    print("Enter the grid row by row:")
    grid = []
    for _ in range(N):
        row = input().strip()
        grid.append(list(row))

    # Call the function
    display_Path_to_Princess(N, grid)
