import pygame
import random as r
import config as c


class Gui(pygame.sprite.Sprite):
    HEART_IMGS = {}
    def __init__(self,screen,p1a1,p1a2,p1a3,p2a1,p2a2,p2a3):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        #FONTS
        self.timer_font = pygame.font.SysFont("default", 30)
        self.timerfontcolor = c.BLACK
        #player1abilities
        self.p1a1 = p1a1/c.FPS
        self.p1a2 = p1a2/c.FPS
        self.p1a3 = p1a3/c.FPS
        #player2abilities
        self.p2a1 = p2a1
        self.p2a2 = p2a2
        self.p2a3 = p2a3
        #EAGLECOLORS
        self.eaglecolor1 = c.GREEN
        self.eaglecolor2 = c.DARKGREEN
        #CHICKENCOLORS
        self.chickencolor1 = c.ORANGE
        self.chickencolor2 = c.RED
        #HEALTH STATUS THINGS
        self.p1hp = 100
        self.p2hp = 100
        self.health_font = pygame.font.SysFont("default", 30)
        self.healthfontcolor = (255, 105, 180)
        self.deadtext = pygame.image.load('assets/PNG/Dead.png')
        self.heartsign = pygame.image.load('assets/PNG/items/life.png')
        self.load_heart_images()

        #ABILITY IMAGES
        self.eagle_supa = pygame.image.load('assets/PNG/Bullets/Villain Bullet E.png')
        self.eagle_supa = pygame.transform.scale(self.eagle_supa, (75, int(25*1.25)))
        self.eagle_supa = pygame.transform.flip(self.eagle_supa, True, False)
        self.chicken_supa = pygame.image.load('assets/PNG/Bullets/Hero Bullet E.png')
        self.chicken_supa = pygame.transform.scale(self.chicken_supa, (75, int(25*1.25)))
        self.chicken_supa = pygame.transform.flip(self.chicken_supa, True, False)
        self.eagle_dash = pygame.image.load('assets/PNG/Bullets/Villain Bullet F.png')
        self.eagle_dash = pygame.transform.scale(self.eagle_dash, (75, 75))
        self.eagle_dash = pygame.transform.flip(self.eagle_dash, True, False)
        self.chicken_dash = pygame.image.load('assets/PNG/Bullets/Hero Bullet F.png')
        self.chicken_dash = pygame.transform.scale(self.chicken_dash, (75, 75))
        self.chicken_dash = pygame.transform.flip(self.chicken_dash, True, False)
        self.eagleimage = pygame.image.load('assets/PNG/hero one - eagle/flying/a1.png')
        self.eagleimage = pygame.transform.scale(self.eagleimage, (36, 30))
        self.chickenimage = pygame.image.load('assets/PNG/hero two - chicken/flying/a1.png')
        self.chickenimage = pygame.transform.scale(self.chickenimage, (36, 30))
        self.chickenimage = pygame.transform.flip(self.chickenimage, True, False)
        self.eagleblock = pygame.image.load('assets/PNG/Bullets/Villain Bullet D.png')
        self.eagleblock = pygame.transform.scale(self.eagleblock, (75, 75))
        self.chickenblock = pygame.image.load('assets/PNG/Bullets/Hero Bullet D.png')
        self.chickenblock = pygame.transform.scale(self.chickenblock, (75, 75))

    def abilityupdate(self,p1a1,p1a2,p1a3,p2a1,p2a2,p2a3,p1hp,p2hp):
        self.p1a1 = p1a1 / c.FPS
        self.p1a2 = p1a2 / c.FPS
        self.p1a3 = p1a3 / c.FPS

        self.p2a1 = p2a1 / c.FPS
        self.p2a2 = p2a2 / c.FPS
        self.p2a3 = p2a3 / c.FPS

        self.p1hp = p1hp
        self.p2hp = p2hp

    def load_heart_images(self):
        for i in range(101):
            Gui.HEART_IMGS[i] = pygame.transform.scale(self.heartsign, (i, i))

    def drawsquare(self,x,y,width,color):
        pygame.draw.polygon(self.screen,color,((x,y),(x + 75,y),(x + 75, y - 75 ),(x,y - 75)),width)
    def update(self):

        #polygon = surface, color, pointlist, width
        #EAGLEGUI
        self.drawsquare(160,485,0,self.eaglecolor1)
        self.drawsquare(160,485,5,self.eaglecolor2)

        self.drawsquare(160+85, 485,0,self.eaglecolor1)
        self.drawsquare(160 + 85, 485, 5, self.eaglecolor2)

        self.drawsquare(165+85+80,485,0,self.eaglecolor1)
        self.drawsquare(165 + 85 + 80, 485, 5, self.eaglecolor2)

        self.p1a1display = self.timer_font.render(f"{self.p1a1}", 1, c.BLACK)
        self.p1a2display = self.timer_font.render(f"{self.p1a2}", 1, c.BLACK)
        self.p1a3display = self.timer_font.render(f"{self.p1a3}", 1, c.BLACK)
        self.readydisplay = self.timer_font.render(f"READY", 1, c.BLACK)
        self.keybindp1a1 = self.timer_font.render(f"1", 1, c.BLACK)
        self.keybindp1a2 = self.timer_font.render(f"2", 1, c.BLACK)
        self.keybindp1a3 = self.timer_font.render(f"3", 1, c.BLACK)

        self.screen.blit(self.eagle_dash, (162 + 85, 410))
        self.screen.blit(self.eagleimage, (162 + 85 + 30, 410 + 20))

        self.screen.blit(self.eagle_supa, (162, 430))
        self.screen.blit(self.eagleblock, (160+85+85,485 - 75))
        self.screen.blit(self.eagleimage, (162 + 190, 430))

        if self.p1a1 > 0:
            self.screen.blit(self.p1a1display, (170, 460))
        if self.p1a2 > 0:
            self.screen.blit(self.p1a2display, (170 + 85, 460))
        if self.p1a3 > 0:
            self.screen.blit(self.p1a3display, (170 + 165, 460))

        if self.p1a1 == 0:
            self.screen.blit(self.readydisplay, (162, 460))
        if self.p1a2 == 0:
            self.screen.blit(self.readydisplay, (162 + 85, 460))
        if self.p1a3 == 0:
            self.screen.blit(self.readydisplay, (162 + 170, 460))

        self.screen.blit(self.keybindp1a1, (162, 410))
        self.screen.blit(self.keybindp1a2, (162 + 85, 410))
        self.screen.blit(self.keybindp1a3, (162 + 170, 410))

        #CHICKENGUI
        self.drawsquare(790, 485, 0, self.chickencolor1)
        self.drawsquare(790, 485, 5, self.chickencolor2)

        self.drawsquare(790 - 85, 485, 0, self.chickencolor1)
        self.drawsquare(790 - 85, 485, 5, self.chickencolor2)

        self.drawsquare(790 - 85 - 85, 485, 0, self.chickencolor1)
        self.drawsquare(790 - 85 - 85, 485, 5, self.chickencolor2)

        self.p2a1display = self.timer_font.render(f"{self.p2a1}", 1, c.BLACK)
        self.p2a2display = self.timer_font.render(f"{self.p2a2}", 1, c.BLACK)
        self.p2a3display = self.timer_font.render(f"{self.p2a3}", 1, c.BLACK)


        self.screen.blit(self.chicken_dash,(800 - 95, 410))
        self.screen.blit(self.chicken_supa,(800 - 10, 430))
        self.screen.blit(self.chickenimage, (800 - 85, 430))

        self.screen.blit(self.chickenblock, (450 + 85 + 85, 485 - 75))
        self.screen.blit(self.chickenimage, (800 - 160, 430))

        self.keybindp2a1 = self.timer_font.render(f"=", 1, c.BLACK)
        self.keybindp2a2 = self.timer_font.render(f" -", 1, c.BLACK)
        self.keybindp2a3 = self.timer_font.render(f"0", 1, c.BLACK)

        if self.p2a1 > 0:
            self.screen.blit(self.p2a1display, (800, 460))
        if self.p2a2 > 0:
            self.screen.blit(self.p2a2display, (800 - 85, 460))
        if self.p2a3 > 0:
            self.screen.blit(self.p2a3display, (800 - 175, 460))

        if self.p2a1 == 0:
            self.screen.blit(self.readydisplay, (792, 460))
        if self.p2a2 == 0:
            self.screen.blit(self.readydisplay, (788 - 80, 460))
        if self.p2a3 == 0:
            self.screen.blit(self.readydisplay, (788 - 165, 460))

        self.screen.blit(self.keybindp2a1, (792, 410))
        self.screen.blit(self.keybindp2a2, (788 - 80, 410))
        self.screen.blit(self.keybindp2a3, (788 - 165, 410))

        p1_heart_img = Gui.HEART_IMGS[self.p1hp]
        p2_heart_img = Gui.HEART_IMGS[self.p2hp]

        if self.p1hp <= 0:
            self.screen.blit(self.deadtext, (35, 430))
        if self.p2hp <= 0:
            self.screen.blit(self.deadtext, (900, 430))
        if self.p1hp > 0:
            pygame.draw.polygon(self.screen, (102, 0, 0), ((4, 438), (4 + 75, 438), (4 + 75, 438 + 22), (4, 438 + 22)), 0)
            self.score_text = self.health_font.render(f" {self.p1hp}", 1, self.healthfontcolor)
            if self.p1hp == 100:
                self.screen.blit(self.score_text, (5, 440))
            else:
                self.screen.blit(self.score_text, (10, 440))
            pygame.draw.circle(self.screen, self.healthfontcolor, (101, 450), 49, 0)
            self.screen.blit(p1_heart_img, ((50 + (100 - self.p1hp)/2), (400 + (100 - self.p1hp)/2)))
        if self.p2hp > 0:
            pygame.draw.polygon(self.screen, (102, 0, 0), ((965, 438), (965 + 55, 438), (965 + 55, 438 + 22), (965, 438 + 22)),0)
            self.score_text = self.health_font.render(f" {self.p2hp}", 1, self.healthfontcolor)
            if self.p2hp == 100:
                self.screen.blit(self.score_text, (975, 440))
            else:
                self.screen.blit(self.score_text,(980,440))
            pygame.draw.circle(self.screen, self.healthfontcolor, (875 + 50, 400 + 50), 49, 0)
            self.screen.blit(p2_heart_img, ((875 + (100 - self.p2hp)/2), (400 + (100 - self.p2hp)/2)))




