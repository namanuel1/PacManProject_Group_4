import pytest
import pygame
from ghost import Ghost
from game_board import GameBoard

@pytest.fixture
def game_board():
    return GameBoard()

@pytest.fixture
def ghost():
    return Ghost(100, 100, (255, 0, 0))

# GameBoard walls
test_positions = [
        (100, 100),  
        (300, 100),    
        (600, 100),  
        (300, 350),  
    ]

'''
Ghosts are able to spawn in the walls of the game board. 
The issue should be fixed by checking if ghosts and walls are colliding when spawning in.
When running the game, the red ghost specifically spawns into one of the walls and cannot move..
'''
# https://docs.pytest.org/en/6.2.x/parametrize.html:
@pytest.mark.parametrize("x, y", test_positions)

def test_ghost_spawn_in_wall(ghost, game_board, x, y):
    ghost.x = x
    ghost.y = y

    ghost_rect = pygame.Rect(
        ghost.x - ghost.radius,
        ghost.y - ghost.radius,
        ghost.radius * 2,
        ghost.radius * 2
    )

    for wall in game_board.walls:
        assert not ghost_rect.colliderect(wall), f"At {x}, {y}  ghost overlaps a wall when spawning"

