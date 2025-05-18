import pygame
from constants import WIDTH, HEIGHT, BACKGROUND_COLOR # type: ignore
from interface import Interface # type: ignore
from game_logic import Game # type: ignore
from utils import borders, display_text, display_victory, human_move, AI_move # type: ignore

# Game Loop

def menu(screen):
    """Display the main menu and play."""
    screen.fill(BACKGROUND_COLOR)
    clock = pygame.time.Clock()

    # title
    display_text(screen, 'Hex', 50, (50, 50))

    # istructions
    text = "Player 1 uses blue, Player 2 uses red."
    display_text(screen, text, 30, (50, 200))
    text = ' - Press 1 for P1 human vs P2 AI'
    display_text(screen, text, 30, (50, 250))
    text = ' - Press 2 for P1 AI vs P2 human'
    display_text(screen, text, 30, (50, 300))
    text = ' - Premi 3 for P1 human vs P2 human'
    display_text(screen, text, 30, (50, 350))
    text = " - Press 4 for P1 AI vs P2 AI (for tests, can't close before the end)"
    display_text(screen, text, 30, (50, 400))

    running = True
    while running:
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    running = False
                    play(screen, 'human', 'AI')
                elif event.key == pygame.K_2:
                    running = False
                    play(screen, 'AI', 'human')
                elif event.key == pygame.K_3:
                    running = False
                    play(screen, 'human', 'human')
                elif event.key == pygame.K_4:
                    running = False
                    play(screen, 'AI', 'AI')
      
def play(screen, player_B, player_R):
    """Run a game session."""
    screen.fill(BACKGROUND_COLOR)
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
            else:
                AI_move(interface, game)
                
            if game.winner == 2:
                    print('Red wins')
                    display_victory(screen, 2)
        
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

        pygame.display.update()    

# MAIN

def main():

    pygame.init()
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.display.set_caption('Hex')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    menu(screen)

    pygame.quit()

main()