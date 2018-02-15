#RPG
import pygame
import sys
import time
import random

colors = []
for r in range(0,256,8):
    for g in range(0,256,8):
        for b in range(0,256,8):
            colors.append((r,g,b))




class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()          

pygame.display.set_caption('Pygame Template')
screen = pygame.display.set_mode((1200,700))

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BLACK = (  0,   0,   0)

clock = pygame.time.Clock()
textPrint = TextPrint()

done = False
while done==False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True 
    screen.fill(WHITE)
    textPrint.reset()
    ###

    def pixel(screen, colors, x, y):
        x-=(5*8)+5
        y-=(5*8)+5
        fill_area = []
        for i in range(0,17):
            for k in range(0,17):
                fill_area.append((x+5*i,y+5*k))
        for i in fill_area:
            color = random.choice(colors)
            screen.fill(color, (i, (5, 5)))
    pixel(screen, colors, 600,350)
    ###
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
        

