import pygame
import os

def main():
    pygame.init()
    screen = pygame.display.set_mode((1440,900))
    pygame.display.set_caption("Brightest Dungeon 2 Anniversary Collector Deluxe Edition")
    launched = True
    fond = pygame.image.load("image/menu.jpg")
    font=pygame.font.Font(None, 24)
    text = font.render("Brightest Dungeon 2",1,(255,255,255))
    screen.blit(text, (300, 300))
    pygame.display.flip()
    screen.blit(fond, (0,0))
    pygame.display.update()
    
    while launched:        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                launched = False
main()