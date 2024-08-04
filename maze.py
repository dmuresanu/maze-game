import random

def generate_maze(size=10):
    maze = [['#' for _ in range(size)] for _ in range(size)]
    start, end = (0, 0), (size - 1, size - 1)
    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'
    
    # Create random paths
    current_pos = list(start)
    while current_pos != list(end):
        maze[current_pos[0]][current_pos[1]] = '.'
        if current_pos[0] < end[0] and (random.choice([True, False]) or current_pos[1] == end[1]):
            current_pos[0] += 1
        elif current_pos[1] < end[1]:
            current_pos[1] += 1
    
    return maze

def save_maze(maze, filename='data/maze.json'):
    import json
    with open(filename, 'w') as file:
        json.dump(maze, file)

def load_maze(filename='data/maze.json'):
    import json
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    maze = generate_maze()
    for row in maze:
        print(' '.join(row))