import pygame
import random as r
import config as c

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen
        self.load_images()
        self.scroller = 0
    def load_images(self):
        self.explosion_images = [pygame.transform.scale(pygame.image.load('assets/PNG/Explosion/a1.png'),(50,50)),
                                 pygame.transform.scale(pygame.image.load('assets/PNG/Explosion/a2.png'),(50,50)),
                                 pygame.transform.scale(pygame.image.load('assets/PNG/Explosion/a3.png'),(50,50)),
                                 pygame.transform.scale(pygame.image.load('assets/PNG/Explosion/a4.png'),(50,50)),
                                 pygame.transform.scale(pygame.image.load('assets/PNG/Explosion/a5.png'),(50,50))
                                 ]
    def update(self):
        self.image = self.explosion_images[self.scroller]
        self.scroller += 1
        if self.scroller >= 5:
            self.kill()
        self.screen.blit(self.image,(self.x ,self.y ))
