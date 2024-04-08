from pygame.locals import *
from UIObject import *
import globals


class UIButton(UIObject):
    def __init__(self, vec2, sprite, textObj, callback, isActive = False, clickable = True):
        super().__init__(vec2, sprite)
        self.textObj = textObj
        self.callback = callback
        self.clickable = clickable
        self.isActive = isActive
        
        self.textObj.pos = self.pos
        
    def update(self, dt, events):
        if(self.clickable == False):
            return
        
        for event in events:
           if event.type == pygame.MOUSEBUTTONUP:
               rect = self.sprite.get_rect(center=(self.pos.x, self.pos.y))
               if rect.collidepoint(event.pos):
                   self.callback()
             
    def draw(self, screen):
        super().draw(screen)
        self.textObj.draw(screen)


        