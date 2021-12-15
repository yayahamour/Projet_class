import pygame
import os


class Music():

    def __init__(self) -> None:
        pygame.mixer.init()
        
    def main_music(self):
        try :
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("Histoire.mp3")
            pygame.mixer.music.play(-1,0,0)
        except:
            os.error("Verifier fichier son")
    
    def victory_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load("Victory.mp3")
        pygame.mixer.music.play()
    
    def up_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load("up.mp3")
        pygame.mixer.music.play()