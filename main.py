import pygame
from constants import WIDTH, HEIGHT, BACKGROUND_COLOR
from interface import Interface
from game_logic import Game
from utils import borders, display_text, display_victory, human_move, AI_move

player_B = 'human'
player_R = 'AI'
state = 'menu'

def menu(screen):
    """Display the main menu."""

    global player_B, player_R, state

    screen.fill(BACKGROUND_COLOR)
    clock = pygame.time.Clock()

    # title
    display_text(screen, 'Hex', 50, (50, 50))

    # istructions
    display_text(screen, "Player 1 uses blue, Player 2 uses red", 30, (50, 200))
    display_text(screen, ' - Press 1 for P1 human vs P2 AI', 30, (50, 250))
    display_text(screen, ' - Press 2 for P1 AI vs P2 human', 30, (50, 300))
    display_text(screen, ' - Press 3 for P1 human vs P2 human', 30, (50, 350))
    display_text(screen, " - Press 4 for P1 AI vs P2 AI (for tests, can't close before the end)", 30, (50, 400))
    display_text(screen, "Warning: it's not possible to close the game while the AI is computing", 30, (50, 500))

    running = True
    while running:
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                state = 'exit'
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player_B = 'human'
                    player_R = 'AI'
                    running = False
                    state = 'play'
                elif event.key == pygame.K_2:
                    player_B = 'AI'
                    player_R = 'human'
                    running = False
                    state = 'play'
                elif event.key == pygame.K_3:
                    player_B = 'human'
                    player_R = 'human'
                    running = False
                    state = 'play'
                elif event.key == pygame.K_4:
                    player_B = 'AI'
                    player_R = 'AI'
                    running = False
                    state = 'play'
      
def play(screen):
    """Run a game session."""

    global state

    screen.fill(BACKGROUND_COLOR)
    text = ' - press SPACE to go back to the menu'
    display_text(screen, text, 30, (50, 650))
    borders(screen)
    interface = Interface(screen)
    interface.update()
    game = Game()

    running = True

    clock = pygame.time.Clock()
    pygame.display.update() # It also has to be set at the beginning in case the first move is by the AI, which takes time


    while running:
            
        clock.tick(60)
        if game.current_player == 1 and game.winner == None:
            if player_B == 'human':
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        human_move(interface, game, pos)
                        break
                    if event.type == pygame.QUIT:
                            running = False
                            state = 'exit'
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            running = False
                            state = 'menu'
            else:
                AI_move(interface, game)

            if game.winner == 1:
                print('Blue wins')
                display_victory(screen, 1)
            
        elif game.current_player == 2 and game.winner == None:
            if player_R == 'human':
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        human_move(interface, game, pos)
                        break
                    if event.type == pygame.QUIT:
                        running = False
                        state = 'exit'
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            running = False
                            state = 'menu'
            else:
                AI_move(interface, game)
                
            if game.winner == 2:
                    print('Red wins')
                    display_victory(screen, 2)
        
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        state = 'exit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
                        state = 'menu'

        pygame.display.update()    

# MAIN

def main():

    pygame.init()
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.display.set_caption('Hex')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while state != 'exit':
        if state == 'menu':
            print(state)
            menu(screen)
        if state == 'play':
            print(state)
            play(screen)
    print(state)

    pygame.quit()

main()