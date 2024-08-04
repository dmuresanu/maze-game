from maze import generate_maze, save_maze
from player import Player

def print_maze(maze, player_pos):
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if (r, c) == player_pos:
                print('P', end=' ')
            else:
                print(maze[r][c], end=' ')
        print()

def main_loop(maze, size):
    player = Player((0, 0))
    
    while True:
        print_maze(maze, player.position)
        move = input("Move (W/A/S/D): ").upper()
        if move == 'Q':
            print("Thanks for playing!")
            break
        
        if not player.move(move, maze):
            print("Invalid move. You hit a wall or out of bounds. Try again.")
        elif player.position == (size - 1, size - 1):
            print("Congratulations! You have reached the end!")
            break

def start_game():
    maze = generate_maze()
    save_maze(maze)
    main_loop(maze, 10)

if __name__ == "__main__":
    start_game()
