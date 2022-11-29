import pygame
import config as c
import random as r
from players import Player
from eagle import Eagle
from chicken import Chicken
from bullets import Bullet
from powerup import Health
from gui import Gui
from explode import Explosion
from background import Background

class BurDie():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
        self.project_name = 'Bur-Die'
        self.background = Background(self.screen)

        pygame.display.set_caption(self.project_name)

        self.groupdefine()
        self.background_group.add(self.background)
#FONTS
        self.winner_font = pygame.font.SysFont("default", 80)
        self.winner_font2 = pygame.font.SysFont("default", 70)
        self.startfont = pygame.font.SysFont("default", 150)

        self.startbkg = pygame.image.load('assets/PNG/Title Screen.png')
        self.ChickenWinbkg = pygame.image.load('assets/PNG/Chicken Win.png')
        self.EagleWinbkg = pygame.image.load('assets/PNG/Eagle Win.png')

        self.hooray1 = pygame.image.load('assets/PNG/Bullets/Villain Bullet B.png')
        self.hooray1 = pygame.transform.scale(self.hooray1, (500,500))
        self.hooray2 = pygame.image.load('assets/PNG/Bullets/Hero Bullet B.png')
        self.hooray2 = pygame.transform.scale(self.hooray2, (500, 500))
        self.controlspage = pygame.image.load('assets/PNG/Controls Page.png')
        self.playimage = pygame.image.load('assets/PNG/play_button.png')
        self.creditsimage = pygame.image.load('assets/PNG/CntrlCred button.png')
        self.creditsbutton = pygame.image.load('assets/PNG/credits_button.png')
        self.mainmenu = pygame.image.load('assets/PNG/Main Menu Buttom.png')
        self.credits = pygame.image.load('assets/PNG/credits.png')
#PLAYER
        self.player1 = Eagle(50,50, self.screen, c.EAGLE_FLY, 90)
        self.player1.type = c.EAGLE_DEAD
        self.player2 = Chicken(c.WIDTH - (50 + 145), 50,self.screen, c.CHICKEN_FLY, 270)
        self.player2.type = c.CHICKEN_DEAD
        self.player_group1.add(self.player1)
        self.player_group2.add(self.player2)
        self.gamemode = c.MAIN_MENU

        self.hittimer1 = 8
#BULLET
        self.bullet_warmup_delay = c.BULLET_WARMUP_DELAY
        self.bullet_warmup_delay2 = c.BULLET_WARMUP_DELAY
#HEART_POWERUP
        self.heart_create_delay = c.HEART_CREATE_DELAY
        self.poweruptimer1 = 200
        self.poweruptimer2 = 200
        self.credits_y = c.HEIGHT

        self.gui = Gui(self.screen,self.player1.ability1cooldown,self.player1.ability2cooldown,self.player1.ability3cooldown,self.player2.ability1cooldown,self.player2.ability2cooldown,self.player2.ability3cooldown)
        self.gui_group.add(self.gui)
        self.powerup_group.add(Health(c.WIDTH/2, c.HEIGHT/2, 50, self.screen, 2))
        self.loadaudioeffects()
        #pygame.mixer.music.play(-1)

        self.running = True

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def groupdefine(self):
        self.background_group = pygame.sprite.GroupSingle()
        self.player_group1 = pygame.sprite.GroupSingle()
        self.player_group2 = pygame.sprite.GroupSingle()
        self.bullet_group1 = pygame.sprite.Group()
        self.bullet_group2 = pygame.sprite.Group()
        self.heart_group = pygame.sprite.Group()
        self.powerup_group = pygame.sprite.Group()
        self.gui_group = pygame.sprite.GroupSingle()
        self.explosion_group = pygame.sprite.Group()

    def loadaudioeffects(self):
        self.dashsfx = pygame.mixer.Sound("assets/Audio/blastoff.wav")
        self.dashsfx.set_volume(0.01)

        self.specialsfx = pygame.mixer.Sound("assets/Audio/blast.wav")
        self.specialsfx.set_volume(0.2)

        self.shootsfx = pygame.mixer.Sound("assets/Audio/plop.wav")
        self.shootsfx.set_volume(0.2)

        self.blocksfx = pygame.mixer.Sound("assets/Audio/transform.wav")
        self.blocksfx.set_volume(0.2)

        self.gothitsfx = pygame.mixer.Sound("assets/Audio/hit3.wav")
        self.gothitsfx.set_volume(0.2)

        self.healpowersfx = pygame.mixer.Sound("assets/Audio/collect2.wav")
        self.healpowersfx.set_volume(0.2)

        self.chargepowersfx = pygame.mixer.Sound("assets/Audio/collect3.wav")
        self.chargepowersfx.set_volume(0.2)

        pygame.mixer.music.load('assets/Audio/background_music.wav')
        pygame.mixer.music.set_volume(0.05)

    def create_heart(self):
        self.heart_group.add(Health(r.randint(50, (1024-50)),r.randint(50, (512-50-80)),50,self.screen,1))

    def create_powerup(self):
        self.powerup_group.add(Health(r.randint(50, (1024-50)),r.randint(50, (512-50-80)),50,self.screen,2))

    def launch_bullet(self,type):
        if self.bullet_warmup_delay == 0:
            self.bullet_group1.add(Bullet(self.player1.x, (self.player1.y + 35), 50, self.player1.direction, type,  self.screen))
            self.shootsfx.play()
            self.bullet_warmup_delay = c.BULLET_WARMUP_DELAY
        else:
            pass

    def launch_bullet2(self,type):
        if self.bullet_warmup_delay2 == 0:
            self.bullet_group2.add(Bullet(self.player2.x, (self.player2.y + 35), 50, self.player2.direction, type,  self.screen))
            self.shootsfx.play()
            self.bullet_warmup_delay2 = c.BULLET_WARMUP_DELAY
        else:
            pass

    def handle_player_alive(self):
        if self.bullet_warmup_delay > 0:
            self.bullet_warmup_delay -= 1

        if self.bullet_warmup_delay2 > 0:
            self.bullet_warmup_delay2 -= 1
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE]:
            self.launch_bullet(1)
        if keys_pressed[pygame.K_RALT]:
            self.launch_bullet2(2)
        if keys_pressed[pygame.K_1]:
            if self.player1.ability1cooldown == 0:
                self.launch_bullet(3)
                self.specialsfx.play()
                self.player1.ability1cooldown = c.ABILITYONECOOLDOWN
        if keys_pressed[pygame.K_EQUALS]:
            if self.player2.ability1cooldown == 0:
                self.launch_bullet2(4)
                self.specialsfx.play()
                self.player2.ability1cooldown = c.ABILITYONECOOLDOWN

        #primaryfirecollides
        pygame.sprite.groupcollide(self.player_group1, self.bullet_group2, False, True, self.player1primarycollide)
        pygame.sprite.groupcollide(self.player_group2, self.bullet_group1, False, True, self.player2primarycollide)
        #supafirecollides
        pygame.sprite.groupcollide(self.player_group1, self.bullet_group2, False, True, self.player1supacollide)
        pygame.sprite.groupcollide(self.player_group2, self.bullet_group1, False, True, self.player2supacollide)
        #healthpowerupcollides
        pygame.sprite.groupcollide(self.player_group1, self.heart_group, False, True, self.healingpowerplayer1)
        pygame.sprite.groupcollide(self.player_group2, self.heart_group, False, True, self.healingpowerplayer2)
        #powerupcollides
        pygame.sprite.groupcollide(self.player_group1, self.powerup_group, False, True, self.abilitycooldownplayer1)
        pygame.sprite.groupcollide(self.player_group2, self.powerup_group, False, True, self.abilitycooldownplayer2)
        #dashcollides
        if self.player1.type == c.EAGLE_DASH:
            self.dashsfx.play()
            pygame.sprite.groupcollide(self.player_group1, self.player_group2, False, False, self.player1dashcollide)
        if self.player2.type == c.CHICKEN_DASH:
            self.dashsfx.play()
            pygame.sprite.groupcollide(self.player_group2, self.player_group1, False, False, self.player2dashcollide)
        pygame.sprite.groupcollide(self.bullet_group1, self.bullet_group2, True, True, self.bulletbulletcollide)

    def handlestartingpage(self):
        self.background_group.update()
        self.screen.blit(self.startbkg, (0, 0))

        playx = (c.WIDTH / 2 + 170) - int(self.playimage.get_width() / 2)
        playy = (c.HEIGHT / 2 + 180) - int(self.playimage.get_height() / 2)
        self.screen.blit(self.playimage, [playx, playy])
        mousex, mousey = pygame.mouse.get_pos()
        if mousex >= playx and mousex <= playx + self.playimage.get_width() and mousey >= playy and mousey <= playy + self.playimage.get_height():
            self.playimage = pygame.transform.scale(self.playimage,(330,88))
        else:
            self.playimage = pygame.image.load('assets/PNG/play_button.png')
        if pygame.mouse.get_pressed()[0]:
            if mousex >= playx and mousex <= playx + self.playimage.get_width() and mousey >= playy and mousey <= playy + self.playimage.get_height():
                self.resetgame()
                self.shootsfx.play()
                self.gamemode = c.GAME_IN_SESSION
#Credits/Control page button
        buttonx = (c.WIDTH / 2 - 170) - int(self.creditsimage.get_width() / 2)
        buttony = (c.HEIGHT / 2 + 180) - int(self.creditsimage.get_height() / 2)
        self.screen.blit(self.creditsimage, [buttonx, buttony])
        if mousex >= buttonx and mousex <= buttonx + self.creditsimage.get_width() and mousey >= buttony and mousey <= buttony + self.creditsimage.get_height():
            self.creditsimage = pygame.transform.scale(self.creditsimage, (330, 88))
        else:
            self.creditsimage = pygame.image.load('assets/PNG/CntrlCred button.png')
        if pygame.mouse.get_pressed()[0]:
            if mousex >= buttonx and mousex <= buttonx + self.creditsimage.get_width() and mousey >= buttony and mousey <= buttony + self.creditsimage.get_height():
                self.shootsfx.play()
                self.gamemode = c.CONTROLS_PAGE
                self.handlecontrolscreditspage()

    def handlecredits(self):
        self.background_group.update()

        self.screen.blit(self.credits, (c.WIDTH/2-(498/2), self.credits_y))
        self.credits_y -= 5
        if self.credits_y == 0-c.HEIGHT-556:
            self.gamemode = c.CONTROLS_PAGE

    def handlecontrolscreditspage(self):
        self.background_group.update()

        buttonx = (c.WIDTH / 2 + 200) - int(self.mainmenu.get_width() / 2)
        buttony = (c.HEIGHT / 2 + 60) - int(self.mainmenu.get_height() / 2)

        buttonx2 = (c.WIDTH / 2 - 200) - int(self.mainmenu.get_width() / 2)
        buttony2 = (c.HEIGHT / 2 + 60) - int(self.mainmenu.get_height() / 2)


        self.screen.blit(self.controlspage, [0,0])
        self.screen.blit(self.mainmenu, [buttonx, buttony])
        self.screen.blit(self.creditsbutton, [buttonx2, buttony2])

        mousex, mousey = pygame.mouse.get_pos()

        if mousex >= buttonx2 and mousex <= buttonx2 + self.mainmenu.get_width() and mousey >= buttony2 and mousey <= buttony2 + self.mainmenu.get_height():
            self.creditsbutton = pygame.transform.scale(self.creditsbutton, (330, 88))
        else:
            self.creditsbutton = pygame.image.load('assets/PNG/credits_button.png')
        if pygame.mouse.get_pressed()[0]:
            if mousex >= buttonx2 and mousex <= buttonx2 + self.mainmenu.get_width() and mousey >= buttony2 and mousey <= buttony2 + self.mainmenu.get_height():
                self.shootsfx.play()
                self.gamemode = c.CREDITS_PAGE
                self.credits_y = c.HEIGHT

        if mousex >= buttonx and mousex <= buttonx + self.mainmenu.get_width() and mousey >= buttony and mousey <= buttony + self.mainmenu.get_height():
            self.mainmenu = pygame.transform.scale(self.mainmenu, (330, 88))
        else:
            self.mainmenu = pygame.image.load('assets/PNG/Main Menu Buttom.png')
        if pygame.mouse.get_pressed()[0]:
            if mousex >= buttonx and mousex <= buttonx + self.mainmenu.get_width() and mousey >= buttony and mousey <= buttony + self.mainmenu.get_height():
                self.shootsfx.play()
                self.gamemode = c.MAIN_MENU

    def healingpowerplayer1(self, player1, heart):
        if player1.rect.colliderect(heart.rect):
            self.player1.lifepoints += 20
            self.healpowersfx.play()
            return True
        else:
            return False
        pass

    def resetgame(self):
        self.player1.make_player_alive()
        self.player1.type = 1
        self.player1.ability1cooldown = 0
        self.player1.ability2cooldown = 0
        self.player1.ability3cooldown = 0

        self.player2.make_player_alive()
        self.player2.type = 2
        self.player1.x = 50
        self.player1.y = 50
        self.player2.y = 50
        self.player2.x = c.WIDTH - (50 + 145)
        self.player2.ability1cooldown = 0
        self.player2.ability2cooldown = 0
        self.player2.ability3cooldown = 0
        self.player1.energy = False
        self.player2.energy = False
        self.player1.direction = 90
        self.player2.direction = 270

        self.powerup_group.empty()
        self.heart_group.empty()

    def abilitycooldownplayer1(self, player1, powerup):
        if player1.rect.colliderect(powerup.rect):
            self.player1.ability1cooldown = 0
            self.player1.ability2cooldown = 0
            self.player1.ability3cooldown = 0
            return True
        else:
            return False
        pass

    def abilitycooldownplayer2(self, player2, powerup):
        if player2.rect.colliderect(powerup.rect):
            self.player2.ability1cooldown = 0
            self.player2.ability2cooldown = 0
            self.player2.ability3cooldown = 0
            return True
        else:
            return False
        pass

    def healingpowerplayer2(self, player2, heart):
        if player2.rect.colliderect(heart.rect):
            self.player2.lifepoints += 20
            self.healpowersfx.play()
            return True
        else:
            return False
        pass

    def player1primarycollide(self,player1,bullet2):
        if player1.rect.colliderect(bullet2.rect):
            if self.player1.type != c.EAGLE_BLOCK and self.player1.type != c.EAGLE_DASH:
                self.player1.type = c.EAGLE_HIT
                self.player1.lifepoints -= 10
                self.gothitsfx.play()
            return True
        else:
            return False
        pass

    def player2primarycollide(self,player2,bullet1):
        if player2.rect.colliderect(bullet1.rect):
            if self.player2.type != c.CHICKEN_BLOCK and self.player1.type != c.EAGLE_DASH:
                self.player2.type = c.CHICKEN_HIT
                self.player2.lifepoints -= 10
                self.gothitsfx.play()
            return True
        else:
            return False

    def player1dashcollide(self,player1,player2):
        if player1.rect.colliderect(player2.rect):
            if self.player2.type != c.EAGLE_BLOCK:
                self.player2.type = c.CHICKEN_HIT
                self.player2.lifepoints -= 20
            self.player1.type = c.EAGLE_FLY
            self.player1.speed = c.PLAYERSPEED
            self.player2.speed = c.PLAYERSPEED
            self.gothitsfx.play()
            return True
        else:
            return False
        pass

    def player2dashcollide(self,player2,player1):
        if player2.rect.colliderect(player1.rect):
            if self.player1.type != c.CHICKEN_BLOCK:
                self.player1.type = c.EAGLE_HIT
                self.player1.lifepoints -= 20
            self.player2.type = c.CHICKEN_FLY
            self.player2.speed = c.PLAYERSPEED
            self.player1.speed = c.PLAYERSPEED
            self.gothitsfx.play()
            return True
        else:
            return False

    def player1supacollide(self, player1, bullet3):
        if player1.rect.colliderect(bullet3.rect):
            self.player1.type = 3
            self.player1.lifepoints -= 40
            self.gothitsfx.play()
            return True
        else:
            return False

    def player2supacollide(self, player2, bullet4):
        if player2.rect.colliderect(bullet4.rect):
            self.player2.type = 4
            self.player2.lifepoints -= 40
            self.gothitsfx.play()
            return True
        else:
            return False

    def bulletbulletcollide(self,bullet1,bullet2):
        if bullet1.rect.colliderect(bullet2.rect):
            if bullet1.type == 3 and bullet2.type == 2:
                bullet2.kill()
                self.gothitsfx.play()
                self.explosion_group.add(Explosion(bullet1.x + 75, bullet2.y - 10, self.screen))
                return False
            if bullet2.type == 4 and bullet1.type == 1:
                bullet1.kill()
                self.gothitsfx.play()
                self.explosion_group.add(Explosion(bullet1.x + 75, bullet2.y - 10, self.screen))
                return False
            self.gothitsfx.play()
            self.explosion_group.add(Explosion(bullet1.x + 75 , bullet2.y - 10,self.screen))
            return True
        else:
            return False

    def cooldownreset(self):
        self.player1.ability1cooldown = 0
        self.player1.ability2cooldown = 0
        self.player1.ability3cooldown = 0
        self.player2.ability1cooldown = 0
        self.player2.ability2cooldown = 0
        self.player2.ability3cooldown = 0
        self.bullet_group2.empty()
        self.bullet_group1.empty()
        self.powerup_group.empty()
        self.heart_group.empty()

    def player1wins(self):
        self.screen.blit(self.EagleWinbkg,(0,0))
        self.cooldownreset()

        playx = (c.WIDTH/2) - int(self.playimage.get_width() / 2)
        playy = (c.HEIGHT/2 + 100) - int(self.playimage.get_height() / 2)

        self.screen.blit(self.playimage, [playx, playy])

        mousex, mousey = pygame.mouse.get_pos()
        if mousex >= playx and mousex <= playx + self.playimage.get_width() and mousey >= playy and mousey <= playy + self.playimage.get_height():
            self.playimage = pygame.transform.scale(self.playimage,(330,88))
        else:
            self.playimage = pygame.image.load('assets/PNG/play_button.png')
        if pygame.mouse.get_pressed()[0]:
            if mousex >= playx and mousex <= playx + self.playimage.get_width() \
                    and \
                    mousey >= playy and mousey <= playy + self.playimage.get_height():
                self.resetgame()
                self.shootsfx.play()
                self.gamemode = c.GAME_IN_SESSION

    def player2wins(self):
        self.screen.blit(self.ChickenWinbkg,(0,0))
        self.cooldownreset()

        playx = (c.WIDTH/2) - int(self.playimage.get_width() / 2)
        playy = (c.HEIGHT/2 + 100) - int(self.playimage.get_height() / 2)
        self.screen.blit(self.playimage, [playx, playy])

        mousex, mousey = pygame.mouse.get_pos()
        if mousex >= playx and mousex <= playx + self.playimage.get_width() and mousey >= playy and mousey <= playy + self.playimage.get_height():
            self.playimage = pygame.transform.scale(self.playimage,(330,88))

        else:
            self.playimage = pygame.image.load('assets/PNG/play_button.png')

        if pygame.mouse.get_pressed()[0]:
            if mousex >= playx and mousex <= playx + self.playimage.get_width() \
                    and \
                    mousey >= playy and mousey <= playy + self.playimage.get_height():
                self.resetgame()
                self.shootsfx.play()
                self.gamemode = c.GAME_IN_SESSION

    def groupupdating(self):
        self.background_group.update()
        self.gui_group.update()
        self.bullet_group1.update()
        self.bullet_group2.update()
        self.heart_group.update()
        self.powerup_group.update()
        self.player_group1.update()
        self.player_group2.update()
        self.explosion_group.update()
        self.gui.abilityupdate(self.player1.ability1cooldown, self.player1.ability2cooldown,
                               self.player1.ability3cooldown, self.player2.ability1cooldown,
                               self.player2.ability2cooldown, self.player2.ability3cooldown,
                               self.player1.lifepoints,self.player2.lifepoints)

    def game_mode_selector(self):
        if self.gamemode == c.MAIN_MENU:
            self.handlestartingpage()
        elif self.gamemode == c.GAME_IN_SESSION:
            self.handle_player_alive()

        elif self.gamemode == c.EAGLE_WIN_PAGE:
            self.player1wins()
        elif self.gamemode == c.CHICKEN_WIN_PAGE:
            self.player2wins()
        elif self.gamemode == c.CONTROLS_PAGE:
            self.handlecontrolscreditspage()
        elif self.gamemode == c.CREDITS_PAGE:
            self.handlecredits()

    def game_loop(self):
        # -------- Main Program Loop -----------
        while self.running:
            # --- Main event loop
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  self.running = False

            pygame.display.flip()

            #self.screen.blit(self.background, (0, 0))

            if c.DEBUG:
                self.powerup_group.add(Health(c.WIDTH / 2, c.HEIGHT / 2, 50, self.screen, 2))

            self.gui_group.update()

            self.groupupdating()

            if self.player1.alive and self.player2.alive:
                self.handle_player_alive()

            self.heart_create_delay -= 1
            if self.heart_create_delay <= 0 and self.player1.alive == True and self.player2.alive == True:
                self.poweruptype = r.randint(1,2)
                if self.poweruptype ==1:
                    self.create_heart()
                elif self.poweruptype ==2:
                    self.create_powerup()
                self.heart_create_delay = c.HEART_CREATE_DELAY

            if self.gamemode == c.CONTROLS_PAGE:
                self.handlecontrolscreditspage()

            self.game_mode_selector()

            if self.player1.alive == True and self.player2.alive == False:
                self.gamemode = c.EAGLE_WIN_PAGE
            elif self.player2.alive == True and self.player1.alive == False:
                self.gamemode = c.CHICKEN_WIN_PAGE

            if c.DEBUG:
                pass

            # --- Limit to 60 frames per second
            self.clock.tick(c.FPS)
            current_fps = str(self.clock.get_fps())
            pygame.display.set_caption(f'{self.project_name}, fps: {current_fps}')

        # Close the window and quit.
        pygame.quit()


if __name__ == '__main__':
    sb = BurDie()
    sb.game_loop()


