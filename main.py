import pygame
import random
import math


pygame.init()

# global constants
class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    
    SIDE_PAD = 100
    TOP_PAD = 150
    
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height 
        
        # set window
        self.window = pygame.display.set_mode((width, height))
        # window title
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        
        self.set_list(lst)
        
    # list attributes    
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        
        self.start_x = self.SIDE_PAD // 2
 
def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    pygame.display.update()
    
def draw_list(draw_info):
    pass 
        
def gen_start_list(n, min_val, max_val):
    lst = []
    
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
            
    return lst

def main():
    run = True
    clock = pygame.time.Clock()
    
    n = 40
    min_val = 1
    max_val = 100
    
    lst = gen_start_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)
    
    
    while run:
        # fps
        clock.tick(60)
        
        draw(draw_info)
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                
    pygame.quit()
 
    
if __name__ == "__main__":
    main()