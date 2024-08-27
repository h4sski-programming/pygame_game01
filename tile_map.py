import pygame
import math
import numpy as np

from settings import *


map_01 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

class TileMap(pygame.Surface):
    def __init__(self) -> None:
        super().__init__(RESOLUTION)
        
        self.tiles: list = []
        self.tiles_dict: dict = {}
        self.generate_map()
        self.draw_tiles()
        self.map_grid = map_01
        self.rect = self.get_rect()
    
    def update(self) -> None:
        self.fill(0)
        self.draw_tiles()
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self, (0, 0))
        # surface.blit(self, (-100, -20))
        
    def draw_tiles(self) -> None:
        for tile in self.tiles:
            tile.draw(self)
    
    def generate_map(self) -> None:
        for row in range(len(map_01)):
            for col in range(len(map_01[0])):
                # if map_01[row][col] == 0:
                #     tile = Tile00(x=col, y=row)
                # else:
                #     tile = Tile01(x=col, y=row)
                self.tiles.append(Tile00(x=col, y=row) if map_01[row][col] == 0 else Tile01(x=col, y=row))
    
    def is_tile_a_wall(self, coords: list) -> bool:
        tile_position = [math.floor(coord/TILE_SIZE) for coord in coords]
        print(tile_position)
        answer = self.map_grid[tile_position[0]][tile_position[1]] == 0
        print(answer)
        return False
        
        
class Tile(pygame.Surface):
    def __init__(self, x: int, y: int, color: tuple, width: int = TILE_SIZE, height: int = TILE_SIZE) -> None:
        # temporary width and height related to resolution
        # width = RESOLUTION[0] // len(map_01[0])
        # height = RESOLUTION[1] // len(map_01)
        
        # super().__init__((width, height))
        super().__init__((width-1, height-1))       ## debug purpouse
        
        self.x: int = x*width
        self.y: int = y*height
        self.position = [self.x, self.y]
        self.image = self
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        
        
        self.fill(color)
    
    def draw(self, surface: pygame.Surface):
        surface.blit(self, (self.x, self.y))
        
        

class Tile00(Tile):
    def __init__(self, x: int, y: int) -> None:
        color = (190, 250, 190)
        super().__init__(x, y, color)

class Tile01(Tile):
    def __init__(self, x: int, y: int) -> None:
        color = (60, 190, 250)
        super().__init__(x, y, color)