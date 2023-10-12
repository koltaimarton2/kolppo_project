import pygame
from Player import Player
class kollpoCity:
    def __init__(self):
        pygame.init()
        self.SCREENSIZE = (800, 800)
        self.SCREEN = pygame.display.set_mode(self.SCREENSIZE)
        self.CLOCK = pygame.time.Clock()
        self.DeltaTime = 0
        self.Frigyes = Player()
        self.Frigyes.PLAYER_POS = pygame.Vector2(self.SCREEN.get_width() / 2, self.SCREEN.get_height() / 2)

    def Start(self):
        running = True
        if(not pygame.get_init()): return
        font = pygame.font.Font()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.SCREEN.fill("white")

            pygame.draw.circle(self.SCREEN, "red", self.Frigyes.PLAYER_POS, 20)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.Frigyes.PLAYER_POS.y -= self.Frigyes.getSpeed() * self.DeltaTime
            if keys[pygame.K_s]:
                self.Frigyes.PLAYER_POS.y += self.Frigyes.getSpeed() * self.DeltaTime
            if keys[pygame.K_a]:
                self.Frigyes.PLAYER_POS.x -= self.Frigyes.getSpeed() * self.DeltaTime
            if keys[pygame.K_d]:
                self.Frigyes.PLAYER_POS.x += self.Frigyes.getSpeed() * self.DeltaTime
            if keys[pygame.K_LSHIFT]: 
                # print(self.Frigyes.RUN)
                self.Frigyes.setRunning(True)
            else:
                # print(self.Frigyes.RUN)
                self.Frigyes.setRunning(False)

            self.DeltaTime = self.CLOCK.tick(60) / 1000

            pygame.display.flip()
        pygame.quit()

newGame = kollpoCity()
newGame.Start()