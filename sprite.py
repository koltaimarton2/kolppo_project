import pygame
from globals import *

class Object(pygame.sprite.Sprite):
    def __init__(self, groups, image = pygame.Surface((TILESIZE, TILESIZE)), position = (0,0), drawLayer: int = 0):
        super().__init__(groups)
        self.drawLayer = drawLayer
        self.image = image
        self.position = position
        self.rect = self.image.get_rect(center = self.position)
    def update(self):
        pass

class CollisionBox:
    def __init__(self, pos = (0, 0), image: pygame.sprite.Sprite = None, size = (0, 0)):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])