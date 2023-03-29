import pygame
import os
os.chdir('C:/Users/ASUS/Desktop/pp2/lab7/mp_lab7/')

pygame.init()
screen = pygame.display.set_mode((350, 500))
pygame.display.set_caption('Player')
button_clicked_image = pygame.image.load('play.png')
button_image = pygame.image.load('pause.png')
button_next = pygame.image.load('next.png')
button_back = pygame.image.load('back.png')
oblozhka = pygame.image.load('oblozhka.png')


button_pos = (150, 400)
button_width = 50
button_height = 50
button_pos_next = (250, 400)
button_pos_back = (50, 400)
button_pos_obl = (35, 50)


button_clicked = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                button_clicked = not button_clicked
            if button_rect_next.collidepoint(event.pos):
                pygame.mixer.music.load('4.mp3')
                pygame.mixer.music.play()
            if button_rect_back.collidepoint(event.pos):
                pygame.mixer.music.load('2.mp3')
                pygame.mixer.music.play()
        # elif event.type == pygame.KEYDOWN:
        #     if  pygame.K_LEFT

        
    screen.fill((255, 255, 0))
    button_image = pygame.transform.scale(button_image, (button_width, button_height))
    button_clicked_image = pygame.transform.scale(button_clicked_image, (button_width, button_height))
    button_next = pygame.transform.scale(button_next, (button_width, button_height))
    button_back = pygame.transform.scale(button_back, (button_width, button_height))
    oblozhka = pygame.transform.scale(oblozhka, (290, 290))

    
    button_rect = button_image.get_rect().move(button_pos)
    button_rect_next = button_next.get_rect().move(button_pos_next)
    button_rect_back = button_back.get_rect().move(button_pos_back) 

    screen.blit(button_next, button_pos_next)
    screen.blit(button_back, button_pos_back)
    screen.blit(oblozhka, button_pos_obl)

    if not button_clicked:
        screen.blit(button_clicked_image, button_pos)
        pygame.mixer.music.load('3.mp3')
        pygame.mixer.music.play()
    else:
        screen.blit(button_image, button_pos)
        # pygame.mixer.music.stop()

    pygame.display.update()
