import pygame

# initialise pygame
pygame.init()
pygame.font.init()

# colors
WHITE = (255, 255, 255) # RGB vals
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

# fps
FPS = 60

# window size 
WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS # integer division

BG_COLOR = WHITE

DRAW_GRID_LINES = False

def get_font(size):
    """
    Generate a font of size [size].
    """
    return pygame.font.SysFont("comicsans", size)