from constants import N, neighbors

class Game:
    """Represents the game state."""
    def __init__(self):
        self.board = [[0] * N for _ in range(N)]
        self.current_player = 1
        self.winner = None
        self.time = 0

    def available_moves(self):
        """Return a list of available moves."""
        return [
            (i, j)
            for i, row in enumerate(self.board)
            for j, value in enumerate(row)
            if value == 0 or self.time == 1
        ]

    def move(self, i, j):
        """Make a move and update the game state."""
        self.board[i][j] = self.current_player
        if self.current_player == 1:
            self.current_player = 2
            if self.time >= 2 * N - 2: # I don't check for victory when its too early
                self.blue_win()
        else:
            self.current_player = 1
            if self.time >= 2 * N - 1:
                self.red_win()
        self.time += 1

    def blue_win(self):
        """Check if the blue player has won."""
        stack = [(i, 0) for i in range(N) if self.board[i][0] == 1]
        visited = set()

        while stack:

            (i, j) = stack.pop()
            if (i, j) in visited:
                continue
            visited.add((i, j))

            for ni, nj in neighbors[(i, j)]:
                if self.board[ni][nj] == 1 and (ni, nj) not in visited:
                    if nj >= N - 1:
                        self.winner = 1
                        return
                    stack.append((ni, nj))

    def red_win(self):
        """Check if the red player has won."""
        stack = [(0, j) for j in range(N) if self.board[0][j] == 2]
        visited = set()
        
        while stack:

            (i, j) = stack.pop()
            if (i, j) in visited:
                continue
            visited.add((i, j))

            for ni, nj in neighbors[(i, j)]:
                if self.board[ni][nj] == 2 and (ni, nj) not in visited:
                    if ni >= N - 1:
                        self.winner = 2
                        return
                    stack.append((ni, nj))