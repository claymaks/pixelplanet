#presets
#pixels are 5x5
#16x16 (80x80)
#3x3 (48x48 [240x240])]
#top left center pixel
#max render = 16x9 chunks
import random
import csv

##
save = "testWorld"
##

biome = [
    "desert",
    "forest",
    "plain",
    "mountain",
    ]

biome_color = [
    "yellow",
    "dark green",
    "light green",
    "grey",
    ]

biome_advantage = [
    "nothing",
    "wood, food",
    "farming",
    "fighting, mining",
    ]


            
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
    
def desert(x, y):
    


    






####################
class biome(object):
    """
    Description:
    
    Attributes:
    """

    def __init__(self, xbot, xtop, ybot, ytop):
        self.xbot = xbot
        self.ybot = ybot
        self.xtop = xtop
        self.ytop = ytop
        
