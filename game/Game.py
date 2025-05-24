import pygame
from game.Grid import Grid
from game.Player import Player

class Game:

    def __init__(self, rows, cols, cell_size):
        pygame.init()
        self.rows=rows
        self.cols = cols
        self.cell_size=cell_size
        self.screen=pygame.display.set_mode((cols * cell_size, rows * cell_size))
        pygame.display.set_caption("XCOPIA")
        self.clock=pygame.time.Clock()
        self.running=True

        #INICIALIZA OBJETOS
        self.grid=Grid(rows, cols, cell_size)
        self.player=Player(0,0, cell_size)



    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move("UP", self.rows, self.cols)
                elif event.key == pygame.K_DOWN:
                    self.player.move("DOWN", self.rows, self.cols)
                elif event.key == pygame.K_LEFT:
                    self.player.move("LEFT", self.rows, self.cols)
                elif event.key == pygame.K_RIGHT:
                    self.player.move("RIGHT", self.rows, self.cols)


    def update(self):
        #ADICIONAR LOGICA DEPOIS
        pass


    def draw(self):
        self.screen.fill((0,0,0))
        self.grid.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60) #60fps limiter

    pygame.quit()