import pygame
import math



class SpriteBase(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, **kwargs) -> None:
        self.x: int = x
        self.y: int = y


class SpriteMovable(SpriteBase):
    def __init__(self, x: float, y: float, velocity: float, **kwargs) -> None:
        super().__init__(x=x, y=y, **kwargs)
        self.velocity: float = velocity
        self.move: bool = False
    
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
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, (self.x, self.y))