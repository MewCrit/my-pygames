import pygame
from random import randint

class Enemies(pygame.sprite.Sprite):

    def __init__(self, type):
        super().__init__()

        self.x_position = 0
        self.frames = []
        y_position = 0

        loader = pygame.image
        
        if type == 'fly':
            fly_frame_1 = loader.load('graphics/Fly/Fly1.png').convert_alpha()
            fly_frame_2 = loader.load('graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_position += 210
        elif type == 'snail':
            snail_frame_1 = loader.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = loader.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_position += 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_position))


    def animation(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation()
        self.rect.x -= 6
        self.destroy()