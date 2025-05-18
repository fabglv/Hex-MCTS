import pygame
import random
from constants import WIDTH, HEIGHT, RED, BLUE
from mcts import MCTS

def display_text(screen, text, font_size, topleft):
    """Display text on the screen."""
    font = pygame.font.Font(None, font_size)
    text = font.render(text , True, (10 ,10 ,10))
    textRect = text.get_rect()
    textRect.topleft = topleft
    screen.blit(text, textRect)

def display_victory(screen, winner):
    """Display victory message."""
    font = pygame.font.Font(None, 100)
    if winner == 1:
        text = font.render('Blu victory' , True, (50,81,198)) # blue
    elif winner == 2:
        text = font.render('Red victory' , True, (101,23,16)) # red
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, textRect)

def borders(screen):
    """Draw borders around the game screen to suggest the directions."""
    rect_n = pygame.Rect((0, 0), (WIDTH, 10))
    rect_s = pygame.Rect((0, HEIGHT - 10), (WIDTH, 10))
    rect_w = pygame.Rect((0, 0), (10, HEIGHT))
    rect_e = pygame.Rect((WIDTH - 10, 0), (10, HEIGHT))
    pygame.draw.rect(screen, RED, rect_n)
    pygame.draw.rect(screen, RED, rect_s)
    pygame.draw.rect(screen, BLUE, rect_w)
    pygame.draw.rect(screen, BLUE, rect_e)


# Functions to connect the game to the interface when a move is made

def AI_move(interface, game):
    """Make a move for the AI player."""
    i, j = MCTS(game)
    color = game.current_player
    game.move(i, j)
    interface.move(i, j, color)
    interface.update()

def human_move(interface, game, pos):
    """Make a move for the human player."""
    pos = pygame.mouse.get_pos()
    i, j = interface.nearest_center(pos)
    color = game.current_player
    if (i, j) in game.available_moves():
        game.move(i, j)
        interface.move(i, j, color)
        interface.update()

def AI_move_random(interface, game):
    """Make a random move, just for testing."""
    i, j = random.choice(game.available_moves())
    color = game.current_player
    game.move(i, j)
    interface.move(i, j, color)
    interface.update()