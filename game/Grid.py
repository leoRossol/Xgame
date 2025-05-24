import pygame

class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows=rows
        self.cols=cols
        self.cell_size=cell_size

    def draw(self, surface):
        for x in range(self.cols+1):
            pygame.draw.line(surface,(50,50,50), (x * self.cell_size, 0), (x * self.cell_size, self.rows * self.cell_size))
        for y in range(self.rows+1):
            pygame.draw.line(surface, (50,50,50), (0, y * self.cell_size), (self.cols * self.cell_size, y * self.cell_size))