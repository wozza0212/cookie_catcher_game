'''
Created on 16 Sep 2021

@author: thomaswasnidge
'''
import os 
import cfg 
import sys 
import pygame 
import random 
from modules import *
from PIL.ImageChops import screen 


def initGame():
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('catch coins')
    
    game_images = {}
    for key, value in cfg.IMAGE_PATHS.items():
        if isinstance(value, list):
            images = []
            for item in value: images.append(pygame.image.load(item))
            game_images[key] = images 
        else:
            game_images[key] = pygame.image.load(value)
            
    game_sounds = {}
    for key, value in cfg.AUDIO_PATHS.items():
        if key == 'bgm': continue 
        game_sounds[key] = pygame.mixer.Sound(value)  
        
    return screen, game_images, game_sounds
        
        
    
    



