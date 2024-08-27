import pygame
import math
import numpy as np

from settings import *
from player import Player
from sprite_custom import SpriteMovable, SpriteDrawable
from tile_map import TileMap


class Enemy(SpriteMovable, SpriteDrawable):
    def __init__(self) -> None:
        super().__init__(x=150, y=230, velocity=20, width=ENEMY_SIZE, height=ENEMY_SIZE, color=ENEMY_COLOR)
                
        # self.image = pygame.Surface((self.width, self.height))
        # self.image.fill(self.color)
        # self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def update(self, dt: float, player: Player, tilemap: TileMap):
        super().update()
        if self.raycast(player, tilemap):
            self.move_towards((player.x, player.y), dt=dt)
        
    
    def raycast(self, player: Player, tilemap: TileMap) -> bool:
        # x_current = self.x + self.width/2
        # y_current = self.y + self.height/2
        
        # for angle in np.arange(0, 2*math.pi, 2*math.pi/16).tolist():
        #     x_current = self.x
        #     y_current = self.y
        #     self.raycast_start_pos = [x_current, y_current]
        #     dx = math.cos(angle)
        #     dy = math.sin(angle)
        #     print(f'{angle = }')
        #     # print(f'{dx = }')
        #     # print(f'{dy = }')
            
        #     # distance = math.sqrt(dx**2 + dy**2)
        #     distance = 100
        #     # print(distance)
            
        #     # dx /= distance
        #     # dy /= distance
            
            
        #     answer = False
        #     for _ in range(int(distance)):
        #         tile_x = int(x_current // TILE_SIZE)
        #         tile_y = int(y_current // TILE_SIZE)
                
        #         if tilemap.map_grid[tile_y][tile_x] == 0:
        #             break
                
        #         x_current += dx
        #         y_current += dy
        #     self.raycast_end_pos = [x_current, y_current]
            
        #     if player.rect.collidepoint(self.raycast_end_pos):
        #         answer = True
        # print(answer)
        
        # def is_wall(coords: list) -> bool:
        #     tile_grid_coords = [int(coords[0]%TILE_SIZE), int(math.floor(coords[1]/TILE_SIZE))]
        #     if tilemap.map_grid[tile_grid_coords[0]][tile_grid_coords[1]] == 0:
        #         return True
        #     return False
        
        for angle in np.arange(0, 2*math.pi+0.1, 2*math.pi/128):
            sin_a = math.sin(angle)
            cos_a = math.cos(angle)
            tan_a = math.tan(angle)
            
            
            enemy_map_pos = np.array([self.x, self.y])
            enemy_tile_pos = np.array([self.x % TILE_SIZE, self.y % TILE_SIZE])
            
            # vertical lines
            first_vert_dx = TILE_SIZE - enemy_tile_pos[0] if cos_a>0 else enemy_tile_pos[0]*-1
            first_vert_dy = first_vert_dx * tan_a
            first_vert_pos = np.array([first_vert_dx, first_vert_dy])
            
            # horizontal lines
            first_hor_dy = TILE_SIZE - enemy_tile_pos[1] if sin_a>0 else enemy_tile_pos[1]*-1
            first_hor_dx = first_hor_dy / tan_a
            first_hor_pos = np.array([first_hor_dx, first_hor_dy])
            
            if not tilemap.rect.collidepoint(first_vert_pos.tolist()):
                continue
            if tilemap.is_tile_a_wall(first_vert_pos.tolist()[:]):
                pygame.draw.line(tilemap, 'purple', enemy_map_pos.tolist(), first_vert_pos.tolist())
                continue
            
            
            next_vert_dx = TILE_SIZE
            next_vert_dy = next_vert_dx * tan_a
            next_vert_pos = np.array([next_vert_dx, next_vert_dy]) + first_vert_pos
            
            
            # x_next_tile = TILE_SIZE - enemy_tile_pos[0]
            # x_first_tile_hit = enemy_map_pos + np.array([x_next_tile, x_next_tile * math.sin(angle)/math.cos(angle)])
            
            # y_next_tile = TILE_SIZE - enemy_tile_pos[1]
            # y_first_tile_hit = enemy_map_pos + np.array([y_next_tile / np.tan(angle), y_next_tile])
            
            pygame.draw.line(tilemap, 'purple', enemy_map_pos.tolist(), first_vert_pos.tolist())
            # pygame.draw.line(tilemap, 'black', enemy_map_pos.tolist(), x_first_tile_hit.tolist())
            # pygame.draw.circle(tilemap, 'black', x_first_tile_hit.tolist(), 2)
        
        x_base_vector = np.array([TILE_SIZE, np.tan(angle)*TILE_SIZE])
        y_base_vector = np.array([TILE_SIZE / np.tan(angle), TILE_SIZE])
        
        # print(x_next_tile)
        # print(x_first_tile_hit)
        
        vector_1 = np.array([1, 2])
        vector_2 = np.array([4, -1])
        # print(np.angle(vector_2))
        
        return True
    
    def draw_raycast(self, surface: pygame.Surface) -> None:
        # pygame.draw.line(surface, self.color, self.raycast_start_pos, self.raycast_end_pos)
        pass