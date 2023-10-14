import pygame
from pytmx.util_pygame import load_pygame
from globals import FONT, BIGFONT, TILESIZE, pygame
from sprite import Object
class mapLoader:
    def __init__(self, pathToMap: str = '', groupReturn: pygame.sprite.Group = None):
        self.tmx_data = load_pygame(pathToMap)
        self.collideTiles = []
        for layer in self.tmx_data.layers:
            if hasattr(layer, 'data') and layer.name:
                for x, y, surf in layer.tiles():
                    pos = (x * TILESIZE, y * TILESIZE)
                    if layer.name.lower() == "floor" or layer.name.lower() == "ground": Object(groupReturn, surf, pos, 0)
                    else: 
                        collideTile = Object(groupReturn, surf, pos, 1)
                        self.collideTiles.append(collideTile)
    
    def get_CollideTiles(self):
        return self.collideTiles

class loadElement(pygame.sprite.Sprite):
    def __init__(self, groups, pathToElement: str = "", size = (0, 0), pos = (0, 0)):
        super().__init__(groups)
        self.path = pathToElement
        self.image = pygame.transform.scale(pygame.image.load(pathToElement).convert_alpha(), size)
        self.rect = self.image.get_rect(center = pos)
    def update(self):
        dSurface = pygame.display.get_surface()
        dSurface.blit(self.image, self.rect)
class textElement(pygame.sprite.Sprite):
    def __init__(self, groups, textInput, position = (0, 0)):
        super().__init__(groups)
        self.text = textInput
        self.font = BIGFONT
        self.base_color, self.hovering_color = (128, 128, 128), (255, 255, 255)
        self.textSurface = self.font.render(self.text, True, self.base_color)
        self.rect = self.textSurface.get_rect(center = position)
    def update(self):
        dSurface = pygame.display.get_surface()
        dSurface.blit(self.textSurface, self.rect)
    def changeColor(self, active):
        if(active):
            self.textSurface = self.font.render(self.text, True, self.hovering_color)
        else:
            self.textSurface = self.font.render(self.text, True, self.base_color)