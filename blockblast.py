from random import randint
import pygame


shapes = [
    [[1, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
]
class Blockblast:
    def __init__(self, width, height, screen_width, screen_height):
        self.height = height
        self.width = width
        self.board = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.score = 0


    def create_board(self, screen):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                position = pygame.Rect(self.screen_width/2 - 175 + j * 60, self.screen_height/2 - 225 + i * 60, 5, 5)
                row.append(Cell(screen, position, (i, j)))
            self.board.append(row)

    
    def draw_board(self,screen, pieces):
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                cellRect = pygame.Rect(self.screen_width/2 - 198 + j * 60, self.screen_height/2 - 248 + i * 60, 58, 58)
    
                if self.board[i][j].is_colliding(pieces):
                    pygame.draw.rect(screen, (233, 226, 13), cellRect)
                elif self.board[i][j].block == 1:
                    pygame.draw.rect(screen, (255, 0, 0), (self.screen_width/2 - 198 + j * 60, self.screen_height/2 - 248 + i * 60, 60, 60))
                else:
                    pygame.draw.rect(screen, (28, 157, 195), cellRect)


    def update_score(self, piece):

        board_t = self.board.copy()
        for i, row in enumerate(self.board):
            blocks = 0
            for j, cell in enumerate(row):
                if cell.block == 1:
                    blocks += 1
            if blocks == len(row):
                self.score += len(row)
                for j, cell in enumerate(row):
                    cell.block = 0

        for i, row in enumerate(board_t):
            blocks = 0
            for j, cell in enumerate(row):
                if board_t[j][i].block == 1:
                    blocks += 1
            if blocks == 9:
                self.score += len(row)
                for j, cell in enumerate(row):
                    self.board[j][i].block = 0

            
                
                


class Cell:
    def __init__(self, screen, position, coord):
        self.screen = screen
        self.position = position
        self.colliding = False
        self.block = 0
        self.coord = coord

    def is_colliding(self, pieces):
        for i, piece in enumerate(pieces):
            for j, block in enumerate(piece.get_rects()):
                if self.position.colliderect(block) and self.block == 0:
                    piece.cells_colliding.append(self.coord)
                    return True
                

class Piece:
    def __init__(self, screen, x=0, y=0):
        self.screen = screen
        self.shape = shapes[randint(0, len(shapes) - 1)]
        self.initial_x = x
        self.initial_y = y
        self.x = x
        self.y = y
        self.dragging = False
        self.block_size = 55
        self.offset_x = 0
        self.offset_y = 0
        self.is_movable = True
        self.cells_colliding = []
        self.blocks = 0

        for i, row in enumerate(self.shape):
            for j, block in enumerate(row):
                if block == 1:
                    self.blocks += 1


    def draw(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    block = pygame.Rect(self.x + j * self.block_size, self.y + i * self.block_size,self.block_size, self.block_size)
                    pygame.draw.rect(self.screen, (255, 0, 0), block)

    def get_rects(self):
        rects = []
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell == 1:
                    rect = pygame.Rect(self.x + j * self.block_size, self.y + i * self.block_size,self.block_size, self.block_size)
                    rects.append(rect)
        return rects

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


    def place(self, board):
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell.is_colliding([self]):
                    cell.block = 1

    
    def is_placeable(self, board):
        cells = 0
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell.is_colliding([self]) and cell.block == 0:
                    cells +=1

        if self.blocks == cells:
            return True
        return False


