from time import sleep
from os import system 
import os
import sys
import pygame
from pygame import mixer

system("cls")
pygame.init()
mixer.init()
pygame.mixer.init()
clock = pygame.time.Clock()

direction = 1
Wind_w = 700
Wind_h = 600
screen = pygame.display.set_mode((Wind_w, Wind_h))

white = (255, 255, 255)
black = (0, 0, 0)
icon = pygame.image.load('Basic Projects\Images\Soul.png')
reset = pygame.mixer.Sound('Basic Projects\Music\ENCOUNTER.mp3')

pygame.display.set_icon(icon)
mixer.music.set_volume(0.7)
mixer.music.load("Basic Projects\Music\ANOTHERHIM.mp3")
mixer.music.play()

class Game:
    '''Where all the window, screen, and background code occurs'''

    def __init__(self):
        # self.title = 'Undertale: Simulation'
        pass

    def window(self, title = '?: Simulation'):
        self.title = title
        pygame.display.set_caption(self.title)

    def text_animation(self, string):
        self.text = ''
        for i in range(len(string)):
            screen.fill(black)
            self.text += string[i]
            font = pygame.font.SysFont('Courier New', 28)
            text_surface = font.render(self.text, True, white)
            text_rect = text_surface.get_rect()
            text_rect.center = (Wind_w/2, Wind_h/2)
            screen.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(300)
        
        sleep(3)

    def background(self):
        screen.fill((0, 0, 0))

class Player:
    global reset
    '''The properties of the Player'''

    def __init__(self, name):
        self.name = name
        self.x = 320
        self.y = 270
        self.img = pygame.image.load('Basic Projects\Images\Soul.png')
        self.img = pygame.transform.scale(self.img, (60, 60))

    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        screen.blit(self.text, self.textRect)

    def draw_flip(self):
        if direction == 1:
            screen.blit(self.img, (self.x, self.y))
        if direction == 0:
            screen.blit(pygame.transform.flip(self.img, True, False), (self.x, self.y))

    def movement(self):
        self.speed = 5
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_s]:
            self.y += self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

        if keys[pygame.K_a]:
            self.x -= self.speed

    def box(self):
        self.draw_box = pygame
        self.box_x = 150
        self.box_y = 100
        self.draw_box.draw.rect(screen, white, pygame.Rect(self.box_x, self.box_y, 400, 400),  2)

    def collision(self):
        if self.x >= 485:
            self.y = 270
            self.x = 320
            pygame.mixer.Sound.play(reset)
        elif self.x <= 145: 
            self.y = 270
            self.x = 320
            pygame.mixer.Sound.play(reset)
        else: pass

        if self.y >= 450: 
            self.y = 270
            self.x = 320
            pygame.mixer.Sound.play(reset)
        elif self.y <= 90:
            self.y = 270
            self.x = 320
            pygame.mixer.Sound.play(reset)
        else: pass

    def Name_tag(self):
        self.dialogue_font = pygame.font.SysFont('Courier New', 28)
        self.text = self.dialogue_font.render('Frisk', True, white, black)
        self.textRect = self.text.get_rect()
        self.textRect.center = (player.x + 30, player.y - 20)



player = Player('Frisk')
game = Game()
game.window('Darkness emgerges...')
game.text_animation('Welcome to the Simulation!')
game.text_animation('Please survive.')
game.text_animation('We do not have much time left.')
game.text_animation('Please just survive and do not screw up...')

while True:
    game.window()
    clock.tick(60)
    game.background()
    player.Name_tag()
    player.draw()
    player.draw_flip()
    player.box()
    player.collision()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_d:
                direction = 1

            if event.type == pygame.K_a:
                direction = 0
        
        player.movement()

    pygame.display.update()

