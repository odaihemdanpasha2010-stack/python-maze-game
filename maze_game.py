"""
Maze Game (Text-Based Robot Simulator)

This program simulates a robot navigating a maze.
The player gives directions (up, down, left, right) to reach the exit
while avoiding walls and staying inside the maze.

Skills used:
- 2D lists
- Loops
- Conditionals
- User input
- Grid navigation logic
"""
maze = [ 
    ['S','W','W','W','W'],
    ['.','.','w','W','W'],
    ['W','.','W','W','W'],
    ['W','.','.','.','.'],
    ['W','W','W','W','E'],
]
row = 0
col = 0
while True:
    if maze[row][col] == 'E':
        print("You win!")
        break
    move = input("Enter your move (up, down, left, right): ")
    if move == "up":
        new_row = row - 1
        new_col = col
        print(new_row , new_col)
    elif move == "down":
        new_row = row + 1
        new_col = col
        print(new_row , new_col)
    elif move == "left":
        new_row = row
        new_col = col - 1
        print(new_row , new_col)
    elif move == "right":
        new_row = row
        new_col = col + 1
        print(new_row , new_col)
    else:
        print("Invalid move. Try again.")
        continue
    if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != 'W':
        row, col = new_row, new_col
    else:
        print("You hit a wall. Try again.")