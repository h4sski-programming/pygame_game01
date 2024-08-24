import pygame

from settings import *
from player import Player
from enemy import Enemy


class Game():
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption('Pygame @ h4sski')
        
        self.is_running: bool
        self.screen = pygame.Surface(RESOLUTION)
        # self.dt: float
        
        self.player = Player()
        self.enemy = Enemy()
    
    
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
    
    
    def update(self) -> None:
        self.player.update()
        self.enemy.update(self.player)
    
    
    def draw(self) -> None:
        self.window.fill(0)
        
        self.enemy.draw(self.window)
        self.player.draw(self.window)
        
        
        pygame.display.flip()
    
    
    def run(self) -> None:
        self.is_running = True
        while self.is_running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()


########################################

if __name__ == '__main__':
    game = Game()
    game.run()