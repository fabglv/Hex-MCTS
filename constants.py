# GAME CONSTANTS
N = 8 # grid size is N x N
TIMEOUT = 5 # seconds available for MCTS

# INTERFACE COSTANTS
HEIGHT = 700
WIDTH = 900
HEX_COLOR = (249,255,233)
BACKGROUND_COLOR = (218,194,178)
BLUE = (152,221,237)
RED = (221,70,21)

# Player 1 is BLUE
# Player 2 is RED

# Precompute directions
directions = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]

# Create neighbors dictionary
neighbors = {}
for i in range(N):
    for j in range(N):
        L = []
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                L.append((ni, nj))
        neighbors[(i, j)] = L