import pygame
import math

from settings import *
from player import Player
from sprite_custom import SpriteMovable, SpriteDrawable
from tile_map import TileMap


class Enemy(SpriteMovable, SpriteDrawable):
    def __init__(self) -> None:
        super().__init__(x=200, y=200, velocity=50, width=TILE_SIZE * 0.6, height=TILE_SIZE * 0.6, color=ENEMY_COLOR)
        
        self.color = ENEMY_COLOR
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def update(self, dt: float, player: Player, tilemap: TileMap):
        if self.raycast(player, tilemap):
            self.move_towards((player.x, player.y), dt=dt)
        
    
    def raycast(self, player: Player, tilemap: TileMap) -> bool:
        dx = player.x - self.x
        dy = player.y - self.y
        
        distance = math.sqrt(dx**2 + dy**2)
        
        dx /= distance
        dy /= distance
        
        x_current = self.x
        y_current = self.y
        
        answer = True
        for _ in range(int(distance)):
            tile_x = int(x_current // TILE_SIZE)
            tile_y = int(y_current // TILE_SIZE)
            
            if tilemap.map_grid[tile_y][tile_x] == 0:
                answer = False
                break
            
            x_current += dx
            y_current += dy
        self.raycast_end_pos = [x_current, y_current]
        return answer
    
    def draw_raycast(self, surface: pygame.Surface) -> None:
        pygame.draw.line(surface, self.color, (self.x, self.y), self.raycast_end_pos)