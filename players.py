import pygame
import random as r
import config as c


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, type, direction, birdtype):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.type = type
        self.screen = screen
        self.direction = direction
        self.birdtype = birdtype

        self.alive = False
        self.lifepoints = 100
        self.lifepointEPIC = self.lifepoints
        self.speed = c.PLAYERSPEED

        self.score_font = pygame.font.SysFont("default", 30)
        self.healthfontcolor = (255,105,180)
        self.deadtext = pygame.image.load('assets/PNG/Dead.png')

        self.actiontimer = 8
        self.blocktimer = 120
        self.energytimer = 200
        self.spritetimer = c.SPRITETIMER
        self.bouncetimer = 10
        self.dashcooldown = 400
        self.dashtimer = 20
        self.scroll = 0

        #ability cooldowns
        self.ability1cooldown = 0
        self.ability2cooldown = 0
        self.ability3cooldown = 0

        self.rect = pygame.Rect(self.x, self.y, 145, 107)

        if self.birdtype == c.EAGLE_BIRD_TYPE:
            self.load_eagle_images()
            self.current_img = self.eagleimages[self.scroll]
            self.dash = pygame.image.load('assets/png/Bullets/Hero Bullet F.png')
        elif self.birdtype == c.CHICKEN_BIRD_TYPE:
            self.load_chicken_images()
            self.current_img = self.chickenimages[self.scroll]
            self.dash = pygame.image.load('assets/png/Bullets/Villain Bullet F.png')

    def scale_image(self, img, size):
        return pygame.transform.scale(img, size)

    def load_chicken_images(self):
        self.chickenimages = []
        for i in range(1,9):
            self.chickenimages.append(self.scale_image(pygame.image.load(f'assets/PNG/hero two - chicken/flying/a{i}.png'),c.PLAYERSIZE))

        self.chickenimagesleft = []
        for x in range(len(self.chickenimages)):
            self.chickenimagesleft.append(pygame.transform.flip(self.chickenimages[x], True, False))

        self.chickenhitimages = [self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/got hit/a1.png'),c.PLAYERHITSIZE),
                                 self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/got hit/a2.png'),c.PLAYERHITSIZE),
                                 self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/got hit/a3.png'),c.PLAYERHITSIZE),
                                 self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/got hit/a4.png'),c.PLAYERHITSIZE),
                                 self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/got hit/a5.png'),c.PLAYERHITSIZE),
                                 self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/got hit/a6.png'),c.PLAYERHITSIZE),
                                 self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/got hit/a7.png'),c.PLAYERHITSIZE),
                                 self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/got hit/a8.png'),c.PLAYERHITSIZE)]

        self.chickenhitimagesleft = []
        for x in range(len(self.chickenhitimages)):
            self.chickenhitimagesleft.append(pygame.transform.flip(self.chickenhitimages[x], True, False))

        self.deadchicken = [self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/faint/a1.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/faint/a2.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/faint/a3.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/faint/a4.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/faint/a5.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/faint/a6.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/faint/a7.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero two - chicken/faint/a8.png'),c.PLAYERSIZE),]

        self.deadchickenleft = []
        for x in range(len(self.deadchicken)):
            self.deadchickenleft.append(pygame.transform.flip(self.deadchicken[x], True, False))

        self.chickenshootimages = [pygame.image.load('assets/PNG/hero two - chicken/shoot/a1.png'),
                                   pygame.image.load('assets/PNG/hero two - chicken/shoot/a2.png'),
                                   pygame.image.load('assets/PNG/hero two - chicken/shoot/a3.png')]

        self.dashimage = pygame.image.load('assets/PNG/Bullets/Hero Bullet F.png')
        self.dashimage = pygame.transform.scale(self.dashimage, (145,127))
        self.blockimage = pygame.image.load('assets/PNG/Bullets/Hero Bullet D.png')
        self.blockimage = pygame.transform.scale(self.blockimage,(200,200))
        self.dashimage2 = pygame.transform.scale(self.dashimage, (145, 127))
        self.dashimage = pygame.transform.flip(self.dashimage, True, False)


    def load_eagle_images(self):
        self.eagleimages = [self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/flying/a1.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/flying/a2.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/flying/a3.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/flying/a4.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/flying/a5.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/flying/a6.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/flying/a7.png'),c.PLAYERSIZE),
                            self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/flying/a8.png'),c.PLAYERSIZE)]
        self.eagleimagesleft = []
        for x in range(len(self.eagleimages)):
            self.eagleimagesleft.append(pygame.transform.flip(self.eagleimages[x],True,False))

        self.eaglehitimages = [self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/got hit/a1.png'),c.PLAYERHITSIZE),
                               self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/got hit/a2.png'),c.PLAYERHITSIZE),
                               self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/got hit/a3.png'),c.PLAYERHITSIZE),
                               self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/got hit/a4.png'),c.PLAYERHITSIZE),
                               self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/got hit/a5.png'),c.PLAYERHITSIZE),
                               self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/got hit/a6.png'),c.PLAYERHITSIZE),
                               self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/got hit/a7.png'),c.PLAYERHITSIZE),
                               self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/got hit/a8.png'),c.PLAYERHITSIZE)]

        self.eaglehitimagesleft = []
        for x in range(len(self.eagleimages)):
            self.eaglehitimagesleft.append(pygame.transform.flip(self.eaglehitimages[x], True, False))

        self.deadeagle = [self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/faint/a1.png'),c.PLAYERSIZE),
                          self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/faint/a2.png'),c.PLAYERSIZE),
                          self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/faint/a3.png'),c.PLAYERSIZE),
                          self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/faint/a4.png'),c.PLAYERSIZE),
                          self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/faint/a5.png'),c.PLAYERSIZE),
                          self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/faint/a6.png'),c.PLAYERSIZE),
                          self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/faint/a7.png'),c.PLAYERSIZE),
                          self.scale_image(pygame.image.load('assets/PNG/hero one - eagle/faint/a8.png'),c.PLAYERSIZE)]

        self.deadeagleleft = []
        for x in range(len(self.deadeagle)):
            self.deadeagleleft.append(pygame.transform.flip(self.deadeagle[x], True, False))

        self.eagleshootimages = [pygame.image.load('assets/PNG/hero one - eagle/shoot/a1.png'),
                                 pygame.image.load('assets/PNG/hero one - eagle/shoot/a2.png'),
                                 pygame.image.load('assets/PNG/hero one - eagle/shoot/a3.png')]



        self.dashimage = pygame.image.load('assets/PNG/Bullets/Villain Bullet F.png')
        self.blockimage = pygame.image.load('assets/PNG/Bullets/Villain Bullet D.png')
        self.blockimage = pygame.transform.scale(self.blockimage,(200,200))
        self.dashimage = pygame.transform.scale(self.dashimage, (145,127))
        self.dashimage2 = pygame.transform.flip(self.dashimage, True, False)

    def scroller(self):
        self.spritetimer -= 1

        if self.spritetimer <= 0:
            self.scroll += 1
            if self.direction == 90:

                if self.type == c.EAGLE_FLY or self.type == c.EAGLE_BLOCK:
                    self.current_img = self.eagleimages[self.scroll]
                elif self.type == c.CHICKEN_FLY or self.type == c.CHICKEN_BLOCK:
                    self.current_img = self.chickenimages[self.scroll]
                elif self.type == c.EAGLE_HIT:
                    self.current_img = self.eaglehitimages[self.scroll]
                elif self.type == c.CHICKEN_HIT:
                    self.current_img = self.chickenhitimages[self.scroll]
                elif self.type == c.EAGLE_DEAD:
                    self.current_img = self.deadeagle[self.scroll]
                elif self.type == c.CHICKEN_DEAD:
                    self.current_img = self.deadchicken[self.scroll]
                if self.scroll >= 7:
                    self.scroll =0
            elif self.direction == 270:
                if self.type == c.EAGLE_FLY or self.type == c.EAGLE_BLOCK or self.type == c.EAGLE_ENERGY:
                    self.current_img = self.eagleimagesleft[self.scroll]
                elif self.type == c.CHICKEN_FLY or self.type == c.CHICKEN_BLOCK or self.type == c.CHICKEN_ENERGY:
                    self.current_img = self.chickenimagesleft[self.scroll]
                elif self.type == c.EAGLE_HIT:
                    self.current_img = self.eaglehitimagesleft[self.scroll]
                elif self.type == c.CHICKEN_HIT:
                    self.current_img = self.chickenhitimagesleft[self.scroll]
                elif self.type == c.EAGLE_DEAD:
                    self.current_img = self.deadeagleleft[self.scroll]
                elif self.type == c.CHICKEN_DEAD:
                    self.current_img = self.deadchickenleft[self.scroll]
                if self.scroll >= 7:
                    self.scroll =0
            self.spritetimer = c.SPRITETIMER

    def make_player_alive(self):
        self.lifepoints = 100
        self.lifepointEPIC = self.lifepoints
        if self.type == c.CHICKEN_DEAD:
            self.x = c.WIDTH - 200
            self.y = 50
        elif self.type == c.EAGLE_DEAD:
            self.x = 50
            self.y = 50

        self.alive = True

    def gyre_movement(self):
        if self.x >= c.WIDTH + 73:
            self.x = -72
        if self.x <= -73:
            self.x = c.WIDTH + 73
        if self.y >= c.HEIGHT + 54:
            self.y = -53
        if self.y <= -54:
            self.y = c.HEIGHT + 53

    def bird_updates(self):
        print("placeholder")

    def update(self):

        self.scroller()

        self.bird_updates()

        if self.alive:
            self.gyre_movement()
        if self.y == -200:
            self.y = -200

        self.rect.x = self.x
        self.rect.y = self.y

        if self.type == c.CHICKEN_DASH or self.type == c.EAGLE_DASH:
            if self.direction == 90:
                self.screen.blit(self.dashimage2, (self.x, self.y - 10))
            else:
                self.screen.blit(self.dashimage, (self.x, self.y - 10))

        if self.type == c.CHICKEN_DEAD or self.type == c.EAGLE_DEAD:
            if self.y != -300:
                self.y -= 1

        self.ability1cooldown -= 1
        if self.ability1cooldown <= 0:
            self.ability1cooldown = 0
        self.ability2cooldown -= 1
        if self.ability2cooldown <= 0:
            self.ability2cooldown = 0
        self.ability3cooldown -= 1
        if self.ability3cooldown <= 0:
            self.ability3cooldown = 0

        if self.lifepoints <= 0:
            self.lifepoints = 0
            self.alive = False
            if self.type == c.EAGLE_FLY or self.type == c.EAGLE_HIT:
                self.type = 5
            elif self.type == c.CHICKEN_FLY or self.type == c.CHICKEN_HIT:
                self.type = 6

        if self.lifepoints >= 100:
            self.lifepoints = 100

        if c.DEBUG:
            pygame.draw.rect(self.screen, (255, 0, 255), self.rect)
            self.ability2cooldown = 0
            self.ability1cooldown = 0
            self.ability3cooldown = 0

        self.screen.blit(self.current_img, (self.x, self.y))

