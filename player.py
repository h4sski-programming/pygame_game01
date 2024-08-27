import pygame

from settings import *
from sprite_custom import SpriteDrawable


class Player(SpriteDrawable):
    def __init__(self) -> None:
        super().__init__(
            x = 520,
            y = 490,
            width = PLAYER_SIZE,
            height = PLAYER_SIZE,
            color = PLAYER_COLOR
        )
        
        self.move_up: bool = False
        self.move_down: bool = False
        self.move_left: bool = False
        self.move_right: bool = False
    
    def update(self, dt: float) -> None:
        super().update()
        if self.move_up:
            self.y -= 1
        if self.move_down:
            self.y += 1
        if self.move_left:
            self.x -= 1
        if self.move_right:
            self.x += 1
        