import pygame
import time

class RPG():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/army.png') #картинка
        self.image2 = pygame.image.load('images/megaknite.png')  # картинка2
        self.rect = self.image.get_rect()       #   квадрат
        self.rect2 = self.image.get_rect()       #   квадрат 2
        self.screen_rect = self.screen.get_rect()   #   квадрат на экране
        self.screen_rect2 = self.screen.get_rect()   #   квадрат на экране 2

        self.rect.centerx = self.screen_rect.centerx    #корды х
        self.rect.centery = self.screen_rect.centery    #корды у
        self.rect2.centerx = self.screen_rect.centerx    #корды х 2
        self.rect2.centery = self.screen_rect.centery    #корды у 2
        self.rect.bottom = self.screen_rect.bottom  # bottom
        self.rect2.bottom = self.screen_rect.bottom  # bottom2

        self.keyUP_a = False
        self.keyUP_w = False
        self.keyUP_d = False
        self.keyUP_s = False

        self.keyUP_left = False
        self.keyUP_up = False
        self.keyUP_right = False
        self.keyUP_down = False
        self.timer = 0
        self.keyUP_f = 0

            #выход
    def output(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect2)

            #стрельба
    def fire(self):
        if self.keyUP_f == 1:

            self.image3 = pygame.image.load('images/bek.png')    #картинка
            self.rect3 = self.image3.get_rect()  # квадрат
            self.screen_rect3 = self.screen.get_rect()  # квадрат на экране 3
            self.rect3.centerx = self.screen_rect.centerx  # корды х 3
            self.rect3.centery = self.screen_rect.centery  # корды у 3
            self.rect3.centerx = self.rect.centerx - 50
            self.rect3.centery = self.rect.centery +50
            self.rect3.bottom = self.screen_rect.bottom  # bottom2
            self.screen.blit(self.image3, self.rect3)

            self.timer +=1
            self.rect3.centerx -=1
            self.rect3.centery -=1





            #движение
    def update_gun(self):
        if self.keyUP_a == True:
            self.rect.centerx -=1
            print('x=',self.rect.centerx)
            if self.rect.centerx<40:
                self.rect.centerx += 1
        elif self.keyUP_d == True:
            self.rect.centerx +=1
            print('x=',self.rect.centerx)
            if self.rect.centerx>850:
                self.rect.centerx -= 1
        elif self.keyUP_w == True:
            self.rect.centery -=1
            print('y=',self.rect.centery)
            if self.rect.centery<-24:
                self.rect.centery += 1
        elif self.keyUP_s == True:
            self.rect.centery +=1
            print('y=',self.rect.centery)
            if self.rect.centery>543:
                self.rect.centery -= 1

    def update_gun2(self):
        if self.keyUP_left == True:
            self.rect2.centerx -=1
            print('x2=',self.rect2.centerx)
            if self.rect2.centerx<40:
                self.rect2.centerx += 1
        elif self.keyUP_right == True:
            self.rect2.centerx +=1
            print('x2=',self.rect.centerx)
            if self.rect2.centerx>850:
                self.rect2.centerx -= 1
        elif self.keyUP_up == True:
            self.rect2.centery -=1
            print('y2=',self.rect2.centery)
            if self.rect2.centery<-24:
                self.rect2.centery += 1
        elif self.keyUP_down == True:
            self.rect2.centery +=1
            print('y2=',self.rect.centery)
            if self.rect2.centery>543:
                self.rect2.centery -= 1