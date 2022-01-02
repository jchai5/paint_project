from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # window
pygame.display.set_caption("Drawing Board") # title on window

def init_grid(rows, cols, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    
    return grid

def draw_grid(window, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            # rect( window, pixel, (x and y positions))
            pygame.draw.rect(window, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    # draw the grid
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(window, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))            
        for j in range(COLS + 1):
            pygame.draw.line(window, BLACK, (j * PIXEL_SIZE, 0), (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))   

def draw(window, grid, buttons):
    window.fill(BG_COLOR) #fill background
    draw_grid(window, grid)

    #draw buttons
    for button in buttons:
        button.draw(window)

    pygame.display.update()


def get_row_col_from_pos(pos):
    x, y = pos
    row = y// PIXEL_SIZE
    col = x // PIXEL_SIZE

    # check if pos is clicked in toolbar
    if row >= ROWS:
        raise IndexError

    return row, col 

########## INITIALISATION ############

run = True
clock = pygame.time.Clock() # for limiting fps
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK # drawing color to start

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25 # button width/height = 50
buttons = [
    # 10px padding, buttons are 50px long
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, BLUE),

    # Button(10, button_y, 50, 50, YELLOW),
    # Button(70, button_y, 50, 50, PURPLE),
    # Button(130, button_y, 50, 50, PINK),
    # Button(190, button_y, 50, 50, GRAY),

    Button(250, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(310, button_y, 50, 50, BLUE, "Clear", BLACK)
]

while run:
    # for limiting fps
    clock.tick(FPS) 
    # listens for exit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # left mouse btn 0, middle 1, right 2
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos() # gives the x, y position of the user's click

            # if we press somewhere not in the grid
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                # if clicked in toolbar
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    
                    # if clicked, set color
                    drawing_color = button.color

                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR) # new grid
                        drawing_color = BLACK


    # draw the window with the function
    draw(WIN, grid, buttons)
pygame.quit()