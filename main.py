import pygame
import sys
from gun import RPG
import controls

def run():
    pygame.init()
    screen = pygame.display.set_mode((820,580))   #sizes
    pygame.display.set_caption('Battlefild 6')  #tite
    bg_color = (64, 224, 208)
    gun = RPG(screen)

    while True:
        controls.events(gun)
        screen.fill(bg_color)
        gun.output()
        gun.update_gun()
        gun.update_gun2()
        gun.fire()

        pygame.display.flip()



run()