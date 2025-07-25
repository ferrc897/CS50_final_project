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
message_text = pygame.font.Font(None, 50)

pieces = []
moving_piece = None
playing = False
lost = False
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
                if moving_piece.is_placeable(game.board):
                    moving_piece.place(game.board)
                    pieces.remove(moving_piece)

                    if len(pieces) == 0:
                        pieces.append(Piece(screen, 40, 130))
                        pieces.append(Piece(screen, 40, 320))
                        pieces.append(Piece(screen, 40, 510))

                else:
                    moving_piece.x = moving_piece.initial_x
                    moving_piece.y = moving_piece.initial_y

                game.update_score(moving_piece)

                moving_piece.dragging = False
                moving_piece = None
                
                if game.lost(pieces):
                    lost = True
                

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
                pieces.append(Piece(screen, 40, 130))
                pieces.append(Piece(screen, 40, 320))
                pieces.append(Piece(screen, 40, 510))
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

        scoreText = button_text.render('Score:', True, white)
        scoreTextRect = scoreText.get_rect()
        scoreTextRect.center = (width/2 - 200, 70)
        screen.blit(scoreText, scoreTextRect)

        score = button_text.render(str(game.score), True, white)
        scoreRect = score.get_rect()
        scoreRect.center = (width/2 - 150, 70)
        screen.blit(score, scoreRect)
                        
        game.draw_board(screen, pieces)

        for piece in pieces:
            piece.draw()

           
        if lost:
            lost_message = message_text.render("You lost", True, white)
            lost_messageRect = lost_message.get_rect()
            lost_messageRect.center = (width/2, height/2)
            screen.blit(lost_message, lost_messageRect)

            new_game = button_text.render("New game", True, black)
            new_gameRect = new_game.get_rect()
            new_gameRect.center = (width/2 - 100, height/2 + 100)
            pygame.draw.rect(screen, white, new_gameRect)
            screen.blit(new_game, new_gameRect)
           
            go_to_menu = button_text.render("Go to menu", True, black)
            go_to_menuRect = new_game.get_rect()
            go_to_menuRect.center = (width/2 + 100, height/2 + 100)
            pygame.draw.rect(screen, white, go_to_menuRect)
            screen.blit(go_to_menu, go_to_menuRect)
    

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                if new_gameRect.collidepoint(mouse):
                    game = BB(9, 9, width, height)
                    lost = False
                    pieces = []
                    pieces.append(Piece(screen, 40, 130))
                    pieces.append(Piece(screen, 40, 320))
                    pieces.append(Piece(screen, 40, 510))

                if go_to_menuRect.collidepoint(mouse):
                    game = BB(9, 9, width, height)
                    lost = False
                    playing = False
                    pieces = []


        pygame.display.flip()
