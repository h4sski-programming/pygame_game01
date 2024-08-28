import pygame

from settings import *
from player import Player
from enemy import Enemy
from tile_map import TileMap


class Game():
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.dt: float = 0
        self.window: pygame.Surface = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption('Pygame @ h4sski')
        
        self.is_running: bool
        self.screen = pygame.Surface(RESOLUTION)
        
        self.player = Player()
        self.enemy = Enemy()
        self.tile_map = TileMap()
    
    
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            
            # if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        self.player.move_up = True if keys[pygame.K_w] else False
        self.player.move_down = True if keys[pygame.K_s] else False
        self.player.move_left = True if keys[pygame.K_a] else False
        self.player.move_right = True if keys[pygame.K_d] else False
        
    
    
    def update(self) -> None:
        # self.player.update(self.dt)
        self.tile_map.update()
        self.enemy.update(self.dt, self.player, self.tile_map)
        # self.player.update(self.dt)
        self.player.update(self.dt, self.tile_map)      # for testing and debug purpose
    
    
    def draw(self) -> None:
        self.window.fill(0)
        self.screen.fill(0)
        
        self.tile_map.draw(self.screen)
        self.enemy.draw(self.screen)
        self.player.draw(self.screen)
    
        self.enemy.draw_raycast(self.screen)
        
        self.window.blit(self.screen, (0, 0))
        pygame.display.flip()
    
    
    def run(self) -> None:
        self.is_running = True
        while self.is_running:
            self.events()
            self.update()
            self.draw()
            self.dt = self.clock.tick() /1000
            ### debug purpose
            # print(self.dt)
        pygame.quit()


########################################

if __name__ == '__main__':
    game = Game()
    game.run()