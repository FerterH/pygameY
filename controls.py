import pygame
import sys

def events(gun):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    gun.keyUP_a = True
                elif event.key == pygame.K_w:
                    gun.keyUP_w = True
                elif event.key == pygame.K_s:
                    gun.keyUP_s = True
                elif event.key == pygame.K_d:
                    gun.keyUP_d = True
                elif event.key == pygame.K_UP:
                    gun.keyUP_up = True
                elif event.key == pygame.K_DOWN:
                    gun.keyUP_down = True
                elif event.key == pygame.K_LEFT:
                    gun.keyUP_left = True
                elif event.key == pygame.K_RIGHT:
                    gun.keyUP_right = True
                elif event.key == pygame.K_f:
                    gun.keyUP_f = 1


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    gun.keyUP_a = False
                elif event.key == pygame.K_s:
                    gun.keyUP_s = False
                elif event.key == pygame.K_d:
                    gun.keyUP_d = False
                elif event.key == pygame.K_w:
                    gun.keyUP_w = False
                elif event.key == pygame.K_UP:
                    gun.keyUP_up = False
                elif event.key == pygame.K_DOWN:
                    gun.keyUP_down = False
                elif event.key == pygame.K_LEFT:
                    gun.keyUP_left = False
                elif event.key == pygame.K_RIGHT:
                    gun.keyUP_right = False
                # elif event.key == pygame.K_f:
                #     gun.keyUP_f = 0
