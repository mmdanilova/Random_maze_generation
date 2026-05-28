
# Random maze generation

## Main idea
Random maze generation using the algorithm Recursive backtracker.
To learn more about the algorithm, follow the link -> https://habr.com/ru/articles/1002460/

## Instruction
The code creates a maze without loops or closed circuits, without inaccessible areas, and with exactly one path from every point to every other point. The resulting maze is defined by a set of zeros and ones, where zero is a passage and one is a wall.

## Usage
* To create a maze, you need to specify the parameters n and m - the lengths of the sides of the maze, after which the finished maze will be displayed as a set of zeros and ones
* A maze is an object that can be created as: maze = Maze(n, m) - n and m is lengths of the sides of the maze
* The maze can be printed: print(maze)
* The maze can be displayed on the screen as a picture using pygame: maze.show()

## Maze example
<img width="260" height="260" alt="image" src="https://github.com/user-attachments/assets/ef56f91d-5d0d-42ef-9ba1-867b0ab64c2c" />

## Project status
finished
