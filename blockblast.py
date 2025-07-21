from random import randint
import pygame


shapes = [
    [[1, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
]
class Blockblast:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = []

    def create_board(self, screen, screen_width, screen_height):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                position = pygame.Rect(screen_width/2 - 198 + i * 60, screen_height/2 - 248 + j * 60, 58, 58)
                row.append(Cell(screen, position))
            self.board.append(row)

    
    def draw_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                cellRect = pygame.Rect(self.board[i][j].position)
                screen = self.board[i][j].screen
                pygame.draw.rect(screen, (28, 157, 195), cellRect)


class Cell:
    def __init__(self, screen, position):
        self.screen = screen
        self.position = position
        self.block = 0


class Piece:
    def __init__(self, screen, x=0, y=0):
        self.screen = screen
        self.shape = shapes[randint(0, len(shapes) - 1)]
        self.initial_x = x
        self.initial_y = y
        self.x = x
        self.y = y
        self.dragging = False
        self.block_size = 60
        self.offset_x = 0
        self.offset_y = 0
        self.is_movable = True


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

