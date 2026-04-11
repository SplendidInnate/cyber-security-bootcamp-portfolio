# Practical Task L1T22:

def minesweeper(grid):
    """
    This function takes a grid with '#' (mines) and '-' (empty)
    and returns a new grid where each '-' is replaced with the number
    of adjacent mines and diagonals.
    """
    rows = len(grid) # Total rows
    columns = len(grid[0]) # Total columns
    result = [] # Grid to store output

    for x in range(rows): # for-loop to loop through rows
        new_row = []

        for y in range(columns): # for-loop to loop through columns
            if grid[x][y] == "#":
                new_row.append("#") # Kepp mine as it is
            else:
                mine_count = 0 # Count nearby miss

                # for-loop to check all directions around cell
                for row in range(x - 1, x + 2): 
                    for column in range(y - 1, y + 2):

                        # Checking if position is valid inside grid
                        if 0 <= row < rows and 0 <= column < columns: 

                            if grid[row][column] == "#":
                                mine_count += 1

                new_row.append(mine_count) # Add count
        result.append(new_row) # Add row to result
    return result    

# Example of an input:
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Output
for row in minesweeper(grid):
    print(row)