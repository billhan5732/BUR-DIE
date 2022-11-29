import pygame
import random as r
import config as c


class Health(pygame.sprite.Sprite):
    def __init__(self, x, y, size, screen, type):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen
        self.speed = c.POWERUPSPEED
        self.type = type
        self.lifetime = 800

        self.heart_power = pygame.image.load('assets/PNG/items/heal.png')
        self.heart_power = pygame.transform.scale(self.heart_power, (int(self.size),int(self.size)))

        self.energy_power = pygame.image.load('assets/PNG/items/invincible.png')
        self.energy_power = pygame.transform.scale(self.energy_power, (int(self.size),int(self.size)))

        self.rect = pygame.Rect(self.x, self.y, self.heart_power.get_width(), self.heart_power.get_height())

    def update(self):
        self.lifetime -= 1

        if self.lifetime == 0:
            self.kill()

        self.rect.x = self.x
        self.rect.y = self.y
        if c.DEBUG:
            pygame.draw.rect(self.screen, (255, 0, 255), self.rect)

        if self.type ==1:
            self.screen.blit(self.heart_power, (self.x, self.y))
        elif self.type ==2:
            self.screen.blit(self.energy_power,(self.x,self.y))

