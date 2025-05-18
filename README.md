# Hex-MCTS

This is a Python implementation of the Hex board game with an AI player powered by Monte Carlo Tree Search (MCTS) algorithm.

## Game Rules
Hex is a two-player board game played on a hexagonal grid. Players take turns placing stones of their color on the board. 
- Player 1 (Blue) tries to connect the left and right sides of the board
- Player 2 (Red) tries to connect the top and bottom sides of the board
The first player to create a complete path connecting their sides wins.

For more info: https://en.wikipedia.org/wiki/Hex_(board_game)

## References
Stuart Russell, Peter Norvig: Artificial Intelligence: A Modern Approach (4th Edition).

## File Structure

```
main.py                  # Main game entry point  
constants.py             # Game and UI constants  
game_logic.py            # Game class and game state logic  
interface.py             # UI components  
mcts.py                  # MCTS algorithm implementation  
utils.py                 # Utility functions for display and game control  
```
