class Player:
    def __init__(self, start_pos):
        self.position = start_pos

    def move(self, direction, maze):
        x, y = self.position
        if direction == 'W':
            new_pos = (x - 1, y)
        elif direction == 'S':
            new_pos = (x + 1, y)
        elif direction == 'A':
            new_pos = (x, y - 1)
        elif direction == 'D':
            new_pos = (x, y + 1)
        else:
            return False

        if self.is_valid_move(new_pos, maze):
            self.position = new_pos
            return True
        return False

    def is_valid_move(self, pos, maze):
        x, y = pos
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
            return maze[x][y] != '#'
        return False

if __name__ == "__main__":
    maze = [
        ['S', '.', '#'],
        ['#', '.', '#'],
        ['#', '.', 'E']
    ]
    player = Player((0, 0))
    moves = ['S', 'S', 'D', 'D', 'U']  # Example moves
    for move in moves:
        player.move(move, maze)
        print(player.position)
