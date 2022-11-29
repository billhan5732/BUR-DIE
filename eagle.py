import pygame
import config as c
from players import Player

class Eagle(Player):
    def __init__(self,x, y, screen, type, direction):
        super().__init__(x,y,screen,type,direction,c.EAGLE_BIRD_TYPE)

    def bird_updates(self):
        #print("Eagle_updates")
        keys_pressed = pygame.key.get_pressed()

        if self.type == c.EAGLE_HIT:
            self.actiontimer -= 1
            if self.actiontimer == 0:
                self.type = c.EAGLE_FLY
                self.actiontimer = 8

        if self.type == c.EAGLE_BLOCK:
            self.blocktimer -= 1
            self.screen.blit(self.blockimage, (self.x - 40, self.y - 50))
            self.speed = c.PLAYERSPEED / 2
            if self.blocktimer < 0:
                self.lifepoints = self.lifepointEPIC
            if self.blocktimer == 0:
                self.lifepointEPIC = self.lifepoints
                self.blocktimer = 120
                self.type = c.EAGLE_FLY
                self.speed = c.PLAYERSPEED

        if self.type == c.EAGLE_DASH:
            self.dashtimer -= 1
            if self.dashtimer == 0:
                self.type = c.EAGLE_FLY
                self.ability2cooldown = c.ABILITYTWOCOOLDOWN
                self.dashtimer = 20
                self.speed = c.PLAYERSPEED

        if self.alive:
            if keys_pressed[pygame.K_a]:
                self.x -= self.speed
                self.direction = 270
            if keys_pressed[pygame.K_d]:
                self.x += self.speed
                self.direction = 90
            if keys_pressed[pygame.K_w]:
                self.y -= self.speed
            if keys_pressed[pygame.K_s]:
                self.y += self.speed
            if keys_pressed[pygame.K_2]:
                if self.ability2cooldown <= 0:
                    self.speed = 35
                    self.type = c.EAGLE_DASH
                    self.ability2cooldown = c.ABILITYTWOCOOLDOWN
            if keys_pressed[pygame.K_3]:
                if self.ability3cooldown <= 0:
                    self.type = c.EAGLE_BLOCK
                    self.ability3cooldown = c.ABILITYTHREECOOLDOWN