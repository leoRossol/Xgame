import pygame

class Player:
    def __init__(self, row, col, cell_size, color=(0,200,255)):
        self.row=row
        self.col=col
        self.cell_size=cell_size
        self.color=color

    def draw (self, surface):
        center_x = self.col * self.cell_size + self.cell_size //2
        center_y = self.row * self.cell_size + self.cell_size //2
        radius = self.cell_size //2-4
        pygame.draw.circle(surface, self.color, (center_x, center_y), radius)