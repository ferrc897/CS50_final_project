import pygame
from blockblast import Blockblast as BB, Piece

pygame.init()
size = width, height = 1000, 800

game = BB(9, 9, width, height)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

black = (0, 0, 0)
white = (255, 255, 255)
blue =  (0, 0, 255)
red = (255, 0, 0)
grey = (100, 100, 100)

title_text = pygame.font.Font(None, 100)
button_text = pygame.font.Font('assets/fonts/arial.ttf', 20)

pieces = []
moving_piece = None
playing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for piece in pieces:
                    if piece.is_clicked(event.pos) and piece.is_movable:
                        piece.dragging = True
                        moving_piece = piece

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and moving_piece:
                moving_piece.place_piece(game.board, pieces)
                pieces.remove(moving_piece)
                moving_piece.dragging = False
                moving_piece = None

        elif event.type == pygame.MOUSEMOTION and moving_piece:
            moving_piece.update_position(event.pos)

    if not game.board:
        game.create_board(screen)
    screen.fill(blue)

    mouse = pygame.mouse.get_pos()

    if not playing:

        titleBackground = pygame.Rect(width/2 - 200, height * 1/4 - 120, 400, 220)
        pygame.draw.rect(screen, (149, 11, 11), titleBackground)
        title = title_text.render('Blockblast', True, red)
        titleRect = title.get_rect()
        titleRect.center = (width/2, height * 1/4)
        screen.blit(title, titleRect)

        button1 = pygame.Rect(width * 2/5 - 40, height * 1/2, 80, 50)
        if button1.collidepoint(mouse):
            pygame.draw.rect(screen, grey, button1)
        else:
            pygame.draw.rect(screen, white, button1)
        button1text =  button_text.render('Play', True, black)
        button1TextRect = button1text.get_rect()
        button1TextRect.center = (width * 2/5, height * 1/2 + 25)
        screen.blit(button1text, button1TextRect)

        button2 = pygame.Rect(width * 3/5 - 40, height * 1/2, 80, 50)
        if button2.collidepoint(mouse):
            pygame.draw.rect(screen, grey, button2)
        else:
            pygame.draw.rect(screen, white, button2)
        button2text = button_text.render('Quit', True, black)
        button2TextRect = button2text.get_rect()
        button2TextRect.center = (width * 3/5, height * 1/2 + 25)
        screen.blit(button2text, button2TextRect)

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            if button1.collidepoint(mouse):
                playing = True
            elif button2.collidepoint(mouse):
                running = False
        
        pygame.display.flip()

    else:

        screen.fill(blue)
        mouse = pygame.mouse.get_pos()
        menuButton = pygame.Rect(40, 40, 100, 60)
        if menuButton.collidepoint(mouse):
            pygame.draw.rect(screen, grey, menuButton)
        else:
            pygame.draw.rect(screen, white, menuButton)
        
        menu = button_text.render('Menu', True, black)
        menuRect = menu.get_rect()
        menuRect.center = (90, 70)
        screen.blit(menu, menuRect)

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            if menuButton.collidepoint(mouse):
                playing = False

        board = pygame.Rect(width/2 - 200, height/2 - 250, 542, 542)
        pygame.draw.rect(screen, (11, 44, 149), board, border_radius=5)
                        
        game.draw_board(pieces)
                

        for piece in pieces:
            piece.draw()
        
        if len(pieces) == 0:
            pieces.append(Piece(screen, 40, 130))
            pieces.append(Piece(screen, 40, 320))
            pieces.append(Piece(screen, 40, 510))

        pygame.display.flip()
