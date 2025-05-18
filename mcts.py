import math
import random
import time
from copy import deepcopy
from constants import TIMEOUT

# Nodes of MCTS

class Node:
    """Represents a node in the MCTS tree."""
    def __init__(self, game, parent, action):
        self.game = game
        self.parent = parent
        self.action = action # action that generates it
        self.u = 0
        self.n = 0
        self.children = []
        self.unused_actions = game.available_moves() # actions not yet used to create children

    def update(self, result):
        """Update the node based on the result."""
        # nodes have the color of the player who just played
        # that is, the opposite color of the current player
        self.n += 1
        if self.game.current_player != result: self.u += 1

    def UCB(self):
        """Calculate the UCB value for selection."""
        return (self.u / self.n) + (math.sqrt(2 * math.log(self.parent.n) / self.n))
    
    def generate_child(self, action):
        """Generate a child node."""
        i, j = action
        new_game = deepcopy(self.game)
        new_game.move(i, j)
        child = Node(new_game, self, action)
        self.children.append(child)
        return child

# Auxiliary functions for MCTS

def selection(node):
    """Select a node based on UCB."""
    # if there's a winner, I return the node
    # if there are children to expand, I also return the node
    # if I have already generated all the children, I choose one and iterate
    if node.game.winner is not None or node.unused_actions: return node  
    while node.children:
        if node.game.winner is not None or node.unused_actions: return node
        node = max(node.children, key=lambda child: child.UCB())
    return node

def expansion(node):
    """Expand a node by generating a child."""
    # If the game is over, I don't need to expand
    if node.game.winner is not None: return node
    if node.unused_actions:
        action = node.unused_actions.pop()
        node = node.generate_child(action)
    return node

def simulation(node):
    """Simulate a game from a node."""
    if node.game.winner is not None: return node.game.winner
    game = deepcopy(node.game)
    while game.winner == None:
        i, j = random.choice(game.available_moves())
        game.move(i,j)
    return game.winner

def backpropagation(node, result):
    """Backpropagate the result to the root."""
    while node is not None:
        node.update(result)
        node = node.parent
        
# MCTS

def MCTS(game):
    """Perform MCTS to find the best move."""
    root = Node(game, None, None)
    timeout_start = time.time()
    simulations = 0

    while time.time() < timeout_start + TIMEOUT:
        simulations += 1
        node = selection(root)
        node = expansion(node)
        result = simulation (node)
        backpropagation (node, result)

    chosen_child = max(root.children, key=lambda child: child.u)
    i, j = chosen_child.action

    print('# Simulations: ', simulations)
    print('Chosen action: ', i, j)

    return i, j  