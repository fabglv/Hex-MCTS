import pygame
import math
from constants import N, HEX_COLOR, BACKGROUND_COLOR, BLUE, RED, HEIGHT, WIDTH

class Hexagon:
    """Represents a hexagonal cell on the board."""

    def __init__(self, screen, center, radius):
        self.screen = screen
        self.center = center
        self.radius = radius
        self.margin = 2
        self.vertices = self.create_vertices(self.radius)
        self.inner_vertices = self.create_vertices(self.radius-self.margin)

    def create_vertices(self, radius):
        x, y = self.center[0], self.center[1]
        vertices = []
        for n in range(6):
            angle = math.pi/6 + math.pi/3 * n
            vertex = (x + radius * math.cos(angle), y + radius * math.sin(angle))
            vertices.append(vertex)
        return vertices

    def draw(self):
        pygame.draw.polygon(self.screen, BACKGROUND_COLOR, self.vertices)
        pygame.draw.polygon(self.screen, HEX_COLOR, self.inner_vertices)

class Stone:
    """Represents a game stone (player piece)."""
    def __init__(self, screen, center, radius, color):
        self.screen = screen
        self.center = center
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

class Interface:
    """Handles game display and user interaction."""
    def __init__(self, screen):
        self.screen = screen
        self.board = self.create_board()
        self.margin = 50 # margin pixels from the window edge
        # the grid changes based on the window size and the number of cells
        self.radius = self.find_radius()
        self.first_center = self.find_first_center()
        self.center_dict = self.create_center_dict()
        self.hex_list = self.create_hex_list()

    def create_board(self):
        """Create an empty game board."""
        board = [[] for n in range(N)]
        for i in range(N):
            for _ in range(N):
                board[i].append(0)
        return board
    
    def move(self, i, j, color):
        """Make a move on the board."""
        self.board[i][j] = color
        self.add_stone_to_board(i, j, color)
    
    def add_stone_to_board(self, i, j, color):
        if color == BLUE:
            self.board[i][j] = 1
        elif color == RED:
            self.board[i][j] = 2

    def find_radius(self):
        """Calculate the hexagon radius."""
        # h_radius is the maximum possible radius for the height
        # w_radius is the maximum possible radius for the width
        # I'm interested in the minimum, which always fits in the window
        h_radius = (HEIGHT - self.margin) / ((N - 1) * 1.5 + 2)
        w_radius = 2 * (WIDTH - self.margin) / (math.sqrt(3) * (3 * N - 1))
        return min(h_radius, w_radius)
    
    def find_first_center(self):
        """Calculate the first center position."""
        x_length = self.radius * math.sqrt(3) * 0.5 * (3 * N - 1)
        y_length = self.radius * ((N - 1) * 1.5 + 2)
        x = (WIDTH - x_length) / 2 + math.sqrt(3) * 0.5 * self.radius
        y = (HEIGHT - y_length) / 2 + self.radius
        return (x, y)
            
    def create_center_dict(self):
        """Create a dictionary of hexagon centers."""
        dict = {}
        x, y = self.first_center[0], self.first_center[1]
        for i in range(N):
            row_offset = self.radius * 0.5 * math.sqrt(3) * i
            center_y = y + 1.5 * self.radius * i
            for j in range(N):
                center_x = x + row_offset + self.radius * math.sqrt(3) * j
                dict[(i, j)] = (center_x, center_y)
        return dict
        
    def create_hex_list(self):
        """Create a list of hexagons."""
        L = []
        for key in self.center_dict.keys():
            center = self.center_dict[key]
            L.append(Hexagon(self.screen, center, self.radius))
        return L

    def draw_hexs(self):
        """Draw all hexagons."""
        for hex in self.hex_list:
            hex.draw()

    def draw_stones(self):
        """Draw all stones on the board."""
        for i in range(N):
            for j in range(N):
                if self.board[i][j] == 1:
                    center = self.center_dict[(i, j)]
                    Stone(self.screen, center, self.radius/2, BLUE).draw()
                elif self.board[i][j] == 2:
                    center = self.center_dict[(i, j)]
                    Stone(self.screen, center, self.radius/2, RED).draw()

    def update(self):
        """Update the display."""
        self.draw_hexs()
        self.draw_stones()
            
    def nearest_center(self, pos):
        """Find the nearest hexagon center to a position."""
        x, y = pos[0], pos[1]
        best_distance = 2*(WIDTH**2+HEIGHT**2)
        for i in range(N):
            for j in range(N):
                x_center, y_center = self.center_dict[(i, j)]
                distance = (x-x_center)**2 + (y-y_center)**2
                if distance < best_distance:
                    best_distance = distance
                    best_row, best_col = i, j
        if best_distance < self.radius**2:
            return (best_row, best_col)
        else: # non on a hexagon
            return (-1, -1)