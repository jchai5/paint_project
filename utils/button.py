from .settings import *

class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, window):
        """
        draw button
        """
        # the rectangle box
        pygame.draw.rect(
            window, self.color, (self.x, self.y, self.width, self.height)
        )
        pygame.draw.rect(
                window, BLACK, (self.x, self.y, self.width, 2) # 2 is outline e.g. 2px 
        )
        # text
        if self.text:
            button_font = get_font(15)
            text_surface = button_font.render(self.text, 1, self.text_color) # 1 is anti-aliasing stuff, not important
            window.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width()/2,
                self.y + self.height / 2 - text_surface.get_height() / 2)) # blit is drawing it
            
 
    def clicked(self, pos):
        """
        is this button clicked
        """
        x, y = pos
        
        if not (x >= self.x and x <= self.x + self.width):
            return False

        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True