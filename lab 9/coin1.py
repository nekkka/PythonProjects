import pygame
import random
import time
from pygame.locals import *
import os
os.chdir('C:/Users/ASUS/Desktop/pp2/lab 8/images')

pygame.init()
width = 400
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GO GO GO")
running = True
fps = pygame.time.Clock()

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (30, 70))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, width - 40),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, width - 40),0) 
        self.weight = (random.randint(1, 4)) 

    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("yellow.png")
        self.image = pygame.transform.scale(self.image, (30, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < width:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     
 

score = 0
P1 = Player()
E1 = Enemy()


enemies = pygame.sprite.Group()
enemies.add(E1)

C1 = Coins()
C2 = Coins()
coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C2)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(pygame.font.match_font('Trebuchet MS'), size)
    text_surface = font.render(text, True, (255, 255 , 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw background
    screen.fill((0, 0, 0))
    oblozhka = pygame.image.load('road.png')
    oblozhka = pygame.transform.scale(oblozhka, (400, 600))
    screen.blit(oblozhka, (0 , 0))
    
    # Update and draw sprites
    P1.update()
    E1.move()
    P1.draw(screen)
    E1.draw(screen)
    C1.move()
    C1.draw(screen)

    
    # Check for collisions
    if pygame.sprite.spritecollideany(P1, coins):
        score += C1.weight #???
        for coin in coins:
            coin.rect.center = (random.randint(30, 370), 0)

    
    # Draw score text
    draw_text(screen, f"Coins: {score}", 25, 200, 10)
    
    # Check for game over
    if pygame.sprite.spritecollideany(P1, enemies):
        end = pygame.image.load('end.jpg')
        end = pygame.transform.scale(end, (400, 600))
        screen.blit(end, (0 , 0))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(1)
        pygame.quit() 
          
    pygame.display.update()
    fps.tick(60)

        
                