from pygame.locals import *
from GameObject import *
import globals


class UIObject(GameObject):
    def __init__(self, vec2, sprite):
        super().__init__(vec2, sprite)
        self.disabled = False
        self.visible = True
             
    def draw(self, screen):
        if(self.visible):
            super().draw(screen)
    
    def reset(self):
        super().reset()
        self.randomizeValues()
        self.passed = False
        self.canCollide = True

        