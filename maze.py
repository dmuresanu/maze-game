import random

def generate_maze(size=10):
    maze = [['#' for _ in range(size)] for _ in range(size)]
    start, end = (0, 0), (size - 1, size - 1)
    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'
    
    # Simple path for demonstration
    for i in range(size):
        maze[i][i] = '.'
    
    return maze

def save_maze(maze, filename='data/maze.json'):
    import json
    with open(filename, 'w') as file:
        json.dump(maze, file)

if __name__ == "__main__":
    maze = generate_maze()
    for row in maze:
        print(' '.join(row))