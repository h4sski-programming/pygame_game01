import pygame

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
        self.generate_map()
        self.draw_tiles()
        self.map_grid = map_01
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self, (0, 0))
        # surface.blit(self, (-100, -20))
        
    def draw_tiles(self) -> None:
        for tile in self.tiles:
            tile.draw(self)
    
    def generate_map(self) -> None:
        for row in range(len(map_01)):
            for col in range(len(map_01[0])):
                if map_01[row][col] == 0:
                    self.tiles.append(Tile00(x=col, y=row))
                else:
                    self.tiles.append(Tile01(x=col, y=row))
        
        
class Tile(pygame.Surface):
    def __init__(self, x: int, y: int, color: tuple, width: int = TILE_SIZE, height: int = TILE_SIZE) -> None:
        # temporary width and height related to resolution
        # width = RESOLUTION[0] // len(map_01[0])
        # height = RESOLUTION[1] // len(map_01)
        
        # super().__init__((width, height))
        super().__init__((width, height))       ## debug purpouse
        
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