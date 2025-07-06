def displayPathToPrincess():
    # Ask for number of rows
    N = int(input("Enter an odd number for grid size (3 <= N < 100): "))
    if N < 3 or N >= 100 or N % 2 == 0:
        print("Invalid input. N must be an odd integer between 3 and 99.")
        return

    print("Enter the grid row by row:")
    grid = []
    for _ in range(N):
        row = input().strip()
        grid.append(list(row))

    # Find positions of bot (m) and princess (p)
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'm':
                bot = (i, j)
            elif grid[i][j] == 'p':
                princess = (i, j)

    # Calculate moves
    row_diff = princess[0] - bot[0]
    col_diff = princess[1] - bot[1]

    # Vertical moves
    if row_diff < 0:
        print("UP\n" * abs(row_diff), end="")
    else:
        print("DOWN\n" * abs(row_diff), end="")

    # Horizontal moves
    if col_diff < 0:
        print("LEFT\n" * abs(col_diff), end="")
    else:
        print("RIGHT\n" * abs(col_diff), end="")

# Run the function
displayPathToPrincess()


