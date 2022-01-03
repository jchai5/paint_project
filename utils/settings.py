import pygame

# initialise pygame
pygame.init()
pygame.font.init()

# colors
WHITE = (255, 255, 255) # RGB vals
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (127, 0, 255)
PINK = (255, 0, 255)
GRAY = (128, 128, 128)

CYAN = (0, 255, 255)
L_GREEN = (153, 255, 51)
L_RED = (255, 153, 153)
D_RED = (153, 0, 76)
D_BLUE = (0, 0, 153)
ORANGE = (255, 128, 0)

L_GRAY = (224, 224, 224)


# fps
FPS = 1000

# window size 
WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH
TOOLBAR_BG = L_GRAY

PIXEL_SIZE = WIDTH // COLS # integer division

BG_COLOR = WHITE

DRAW_GRID_LINES = False

def get_font(size):
    """
    Generate a font of size [size].
    """
    return pygame.font.SysFont("comicsans", size)