import pygame

from settings import *
from sprite_custom import SpriteDrawable


class Player(SpriteDrawable):
    def __init__(self) -> None:
        super().__init__(
            x = RESOLUTION[0]/2 - TILE_SIZE/2,
            y = RESOLUTION[1]/2 - TILE_SIZE/2,
            width = TILE_SIZE * 0.6,
            height = TILE_SIZE * 0.6,
            color = PLAYER_COLOR
        )
        
        self.move_up: bool = False
        self.move_down: bool = False
        self.move_left: bool = False
        self.move_right: bool = False
    
    def update(self, dt: float) -> None:
        super().update(self)
        if self.move_up:
            self.y -= 1
        if self.move_down:
            self.y += 1
        if self.move_left:
            self.x -= 1
        if self.move_right:
            self.x += 1
        