import pygame
import config as c
from players import Player


class Chicken(Player):
    def __init__(self, x, y, screen, type, direction):
        super().__init__(x, y, screen, type, direction, c.CHICKEN_BIRD_TYPE)

    def bird_updates(self):
        #print("Chicken_update")
        keys_pressed = pygame.key.get_pressed()
        if self.type == c.CHICKEN_HIT:
            self.actiontimer -= 1
            if self.actiontimer == 0:
                self.type = c.CHICKEN_FLY
                self.actiontimer = 8

        if self.type == c.CHICKEN_BLOCK:
            self.blocktimer -= 1
            self.screen.blit(self.blockimage, (self.x - 30, self.y - 50))
            self.speed = c.PLAYERSPEED / 2
            if self.blocktimer < 0:
                self.lifepoints = self.lifepointEPIC
            if self.blocktimer == 0:
                self.lifepointEPIC = self.lifepoints
                self.blocktimer = 120
                self.type = c.CHICKEN_FLY
                self.speed = c.PLAYERSPEED

        if self.type == c.CHICKEN_DASH:
            self.dashtimer -= 1
            if self.dashtimer == 0:
                self.type = c.CHICKEN_FLY
                self.ability2cooldown = c.ABILITYTWOCOOLDOWN
                self.dashtimer = 20
                self.speed = c.PLAYERSPEED

        if self.alive:
            if keys_pressed[pygame.K_l]:
                self.x -= self.speed
                self.direction = 270
            if keys_pressed[pygame.K_QUOTE]:
                self.x += self.speed
                self.direction = 90
            if keys_pressed[pygame.K_p]:
                self.y -= self.speed
            if keys_pressed[pygame.K_SEMICOLON]:
                self.y += self.speed
            if keys_pressed[pygame.K_MINUS]:
                if self.ability2cooldown <= 0:
                    self.speed = 35
                    self.type = c.CHICKEN_DASH
                    self.ability2cooldown = c.ABILITYTWOCOOLDOWN
            if keys_pressed[pygame.K_0]:
                if self.ability3cooldown <= 0:
                    self.type = c.CHICKEN_BLOCK
                    self.ability3cooldown = c.ABILITYTHREECOOLDOWN