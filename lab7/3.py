import pygame

pygame.init()
width = 400
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MOOOOOOVE")
running = True
x = 30
y = 30

ball_Change = 3

clock = pygame.time.Clock()

while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                
        screen.fill((255, 255, 255))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= ball_Change
        if pressed[pygame.K_DOWN]: y += ball_Change
        if pressed[pygame.K_LEFT]: x -= ball_Change
        if pressed[pygame.K_RIGHT]: x += ball_Change
        

        # if x + 50 >= width or x <= 0:
        #         ball_Change *= -1
        # if y + 50 >= height or y <= 0:
        #         ball_Change *= -1
        # x += ball_Change
        # y += ball_Change
        

        if x + 25 >= width:
                x = width - 25
        elif x - 25 <= 0:
                x = 25
        if y + 25 >= height:
                y = height - 25
        elif y - 25 <= 0:
                y = 25


        pygame.draw.circle(screen, (238,130,238), (x, y), 25)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)