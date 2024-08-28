import pygame
import math
import numpy as np



class SpriteBase(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, **kwargs) -> None:
        self.x: int = x
        self.y: int = y
        self.position = np.array([self.x, self.y])


class SpriteMovable(SpriteBase):
    def __init__(self, x: float, y: float, velocity: float, **kwargs) -> None:
        super().__init__(x=x, y=y, **kwargs)
        self.velocity: float = velocity
        self.move: bool = False
    
    def update(self) -> None:
        super().update()
        self.position = np.array([self.x, self.y])
    
    def move_towards(self, destination: tuple, dt: float) -> None:
        dx = destination[0] - self.x
        dy = destination[1] - self.y
        distance = math.sqrt(dx**2 + dy**2)
        self.x += self.velocity * dx/distance * dt
        self.y += self.velocity * dy/distance * dt



class SpriteDrawable(SpriteBase):
    def __init__(self, x: float, y: float, width:float, height:float, color: tuple, **kwargs) -> None:
        super().__init__(x=x, y=y, **kwargs)
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(left=self.x, top=self.y)
    
    
    def update(self) -> None:
        super().update()
        self.rect = self.image.get_rect(left=self.x, top=self.y)
        
        
    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.width/2)
        # surface.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(surface, 'white', self.rect, 3)