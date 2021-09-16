'''
Created on 16 Sep 2021

@author: thomaswasnidge
'''
import pygame 
import random 

class Food(pygame.sprite.Sprite):
    def __init__(self, images_dict, selected_key, screensize, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.screensize = screensize
        self.images = images_dict[selected_key]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = random.randint(20, screensize[0] - 20), -10
        self.speed = random.randrange(5, 10)
        self.socre = 1 if selected_key == 'gold' else 5
        
    def update(self):
        self.rect.bottom += self.speed
        if self.rect.top > self.screensize[1]:
            return True 
        return False 
    
    