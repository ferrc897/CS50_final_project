import pygame

pygame.init()
size = width, height = 1000, 600

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

black = (0, 0, 0)
white = (255, 255, 255)
blue =  (0, 0, 255)
red = (255, 0, 0)
grey = (100, 100, 100)

title_text = pygame.font.Font(None, 100)
button_text = pygame.font.Font('arial.ttf', 20)

playing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    else:
        pass


    pygame.display.flip()
