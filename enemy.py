import pygame
import math

from settings import *
from player import Player


class Enemy(pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.x = TILE_SIZE
        self.y = TILE_SIZE
        
        self.color = ENEMY_COLOR
        self.velocity = 2
        
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def update(self, player: Player):
        dx = player.x - self.x
        dy = player.y - self.y
        rrr = math.sqrt(dx**2 + dy**2)
        self.x += self.velocity * math.sin(player.x/rrr)
        self.y += self.velocity * math.cos(player.y/rrr)
        # self.x += self.velocity * math.cos(player.x/self.x)
        # self.y += self.velocity * math.sin(player.y/self.y)
        
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, (self.x, self.y))