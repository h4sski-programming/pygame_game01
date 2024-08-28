import math
import numpy as np
import pygame

from settings import *
from sprite_custom import SpriteMovable, SpriteDrawable
from tile_map import TileMap


class Player(SpriteMovable, SpriteDrawable):
    def __init__(self) -> None:
        super().__init__(
            x = 520,
            y = 490,
            velocity=100,
            width = PLAYER_SIZE,
            height = PLAYER_SIZE,
            color = PLAYER_COLOR,
        )
        
        self.move_up: bool = False
        self.move_down: bool = False
        self.move_left: bool = False
        self.move_right: bool = False
    
    def update(self, dt: float, tilemap: TileMap) -> None:
        super().update()
        direction = self.position.tolist()
        if self.move_up:
            direction[1] = 0
        if self.move_down:
            direction[1] = RESOLUTION[1]
        if self.move_left:
            direction[0] = 0
        if self.move_right:
            direction[0] = RESOLUTION[0]
        
        if not direction == self.position.tolist():
            self.move_towards(direction, dt=dt)
            
    #     self.testing(tilemap)
    
    # def testing(self, tilemap: TileMap) -> None:
    #     # tile_coords = tilemap.get_tile_coords(self.position)
    #     is_wall = tilemap.is_tile_a_wall(self.position)
    #     # print(tile_coords)
    #     print(is_wall)
        