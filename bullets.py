import pygame
import random as r
import config as c

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x, y, size, direction, type, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen
        self.size = size
        self.direction = direction
        self.type = type
        self.speed = c.PRIMARYFIRESPEED
        self.eagle_bullet = pygame.image.load('assets/PNG/Bullets/Villain Bullet A.png')
        self.eagle_bullet = pygame.transform.scale(self.eagle_bullet, (int(self.size * 2), int(self.size/2)))
        self.chicken_bullet = pygame.image.load('assets/PNG/Bullets/Hero Bullet A.png')
        self.chicken_bullet = pygame.transform.scale(self.chicken_bullet, (int(self.size * 2), int(self.size/2)))

        #SPECIALS
        self.eagle_supa = pygame.image.load('assets/PNG/Bullets/Villain Bullet E.png')
        self.eagle_supa = pygame.transform.scale(self.eagle_supa, (int(self.size * 2), self.size))
        self.chicken_supa = pygame.image.load('assets/PNG/Bullets/Hero Bullet E.png')
        self.chicken_supa = pygame.transform.scale(self.chicken_supa, (int(self.size * 2), self.size))


# bullet changing directions
        if self.direction == 90:
           self.eagle_bullet = pygame.transform.flip(self.eagle_bullet, True, False)
           self.eagle_supa = pygame.transform.flip(self.eagle_supa, True, False)

        if self.direction == 270:
           self.chicken_bullet = pygame.transform.flip(self.chicken_bullet, True, False)
           self.chicken_supa = pygame.transform.flip(self.chicken_supa, True, False)

        self.image = self.eagle_bullet
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())


        if self.type == 1:
           self.image = self.eagle_bullet
        else:
           self.image = self.chicken_bullet

        if self.type == 3:
            self.image = self.eagle_supa
        elif self.type == 4:
            self.image = self.chicken_supa

        if self.type == 3 or self.type == 4:
            self.speed = c.SUPASPEED


    def update(self):

       if self.x > c.WIDTH or self.x < 0:
           self.kill()

       if self.direction == 90:
           self.x += self.speed
       else:
           self.x -= self.speed

       self.rect.x = self.x
       self.rect.y = self.y

       if c.DEBUG:
           pygame.draw.rect(self.screen, (255, 0, 255), self.rect)

       self.screen.blit(self.image, (self.x, self.y))









