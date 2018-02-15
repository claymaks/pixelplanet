#presets
#pixels are 5x5
#16x16 (80x80)
#3x3 (48x48 [240x240])]
#top left center pixel
import random

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
def pixel(screen, colors, x, y):
    x-=(5*8)+5
    y-=(5*8)+5
    fill_area = []
    for i in range(0,17):
        for k in range(0,17):
            fill_area.append(x+5*i,y+5*k)
    for i in fill_area:
        color = random.choice(colors)
        screen.fill(color, (i, (5, 5)))
    
def desert(x, y):
    

def pre_gen():
    






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
        
