import pygame

class cameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        self.zoom_scale = 3
        self.internal_surface_size = (1000, 1000)
        self.internal_surface = pygame.Surface(self.internal_surface_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surface.get_rect(center = (self.half_w, self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surface_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surface_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surface_size[1] // 2 - self.half_h
    def centerCam(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def draw(self, target) -> None:
        self.centerCam(target)

        self.internal_surface.fill('lightblue')

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            if (sprite.drawLayer == 0):
                self.internal_surface.blit(sprite.image, offset_pos)
        for sprite in sorted(self.sprites(), key = lambda sprite : sprite.rect.center):
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            if(sprite.drawLayer != 0): self.internal_surface.blit(sprite.image, offset_pos)
        
        scaled_surface = pygame.transform.scale(self.internal_surface, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surface.get_rect(center = (self.half_w, self.half_h))
        self.display_surface.blit(scaled_surface, scaled_rect)