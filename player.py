import pygame

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        
        self.x = RESOLUTION[0]/2
        self.y = RESOLUTION[1]/2
        self.color = PLAYER_COLOR
        
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        # self.image.fill('green')
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect)