#RPG
import pygame
import sys
import time
import random
import csv

##
save = "testWorld"
##

colors = []
for r in range(0,256,8):
    for g in range(0,256,8):
        for b in range(0,256,8):
            colors.append((r,g,b))
           
def init(save, l):
    file = save + ".csv"
    fw = open(file, 'w', newline='')
    w = csv.writer(fw, dialect='excel')
    w.writerows(l)
    fw.close()

def pregen_pixel(screen, save, x, y):
    x-=(5*8)+5
    y-=(5*8)+5
    fill_area = []
    for i in range(0,17):
        for k in range(0,17):
            fill_area.append((x+5*i,y+5*k))
    file = save + ".csv"
    fr = open(file, 'r')
    r = csv.reader(fr)
    biocolorsCSV = list(r)
    biocolors = []
    for i in biocolorsCSV:
        rgb = []
        for k in i:
            rgb.append(int(k))
        biocolors.append(rgb)
    for i,k in enumerate(fill_area):
        screen.fill(biocolors[i], (k, (5, 5)))
    fr.close()

def first_gen(screen, colors, x, y):
    x-=(5*8)+5
    y-=(5*8)+5
    fill_area = []
    for i in range(0,17):
        for k in range(0,17):
            fill_area.append((x+5*i,y+5*k))
    tile = []
    for i in fill_area:
        color = random.choice(colors)
        screen.fill(color, (i, (5, 5)))
        tile.append(color)
    init(save, tile)


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


first_gen(screen, colors, 600, 350)

done = False
while done==False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True 
    screen.fill(WHITE)
    textPrint.reset()
    ###

    
    pregen_pixel(screen, save, 600, 350)

    ###
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
        

