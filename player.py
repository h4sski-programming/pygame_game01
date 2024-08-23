import pygame

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        
        self.x = 100
        self.y = 70
        
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill('green')
        self.rect = self.image.get_rect()