from random import randint
import pygame


shapes = [
    [[1, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 1, 0], [1, 1, 1]]
]
class Blockblast:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.board = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(False)
            self.board.append(row)

class Piece:
    def __init__(self, screen, x=0, y=0):
        self.screen = screen
        self.shape = shapes[randint(0, len(shapes) - 1)]
        self.x = x
        self.y = y
        self.dragging = False
        self.block_size = 60
        self.offset_x = 0
        self.offset_y = 0


    def draw(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    block = pygame.Rect(self.x + j * self.block_size, self.y + i * self.block_size,self.block_size, self.block_size)
                    pygame.draw.rect(self.screen, (255, 0, 0), block)


    def is_clicked(self, pos):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    rect = pygame.Rect(self.x + j * self.block_size, self.y + i * self.block_size,self.block_size, self.block_size)

                    if rect.collidepoint(pos):
                        self.offset_x = self.x - pos[0]
                        self.offset_y = self.y - pos[1]
                        return True
        return False
    
    def update_position(self, pos):
        if self.dragging:
            self.x = self.offset_x + pos[0]
            self.y = self.offset_y + pos[1]

