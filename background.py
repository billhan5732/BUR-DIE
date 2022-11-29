import pygame
import config as c

class Background(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.background = pygame.image.load('assets/PNG/Background1/Bkg.png')
        self.screen = screen
        self.x = 0
        self.y = 0

    def update(self):
        if self.x != -c.WIDTH:
            self.x -= 1
        elif self.x == -c.WIDTH:
            self.x = 0
        self.screen.blit(self.background,(self.x,self.y))