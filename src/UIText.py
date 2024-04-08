from pygame.locals import *
from UIObject import *
import globals


class UIText(UIObject):
    def __init__(self, vec2, sprite, font ,text, colour):
        super().__init__(vec2, sprite)
        self.font = font
        self.text = text
        self.colour = colour
             
    def draw(self, screen):
        self.sprite = self.font.render(self.text, True, self.colour)
        super().draw(screen)


        