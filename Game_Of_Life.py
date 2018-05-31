import pygame
import sys
import time
import numpy
from random import randint
import random
pygame.init() #pygame initilization
width = 800 #resolution
height = 800
total = 100
WHITE = (255,255,255) #set color
BLACK = (0,0,0)
pygame.display.set_caption("Game Of Life")
per_width = int(round(width / total)) #panel area
per_height = int(round(height / total))
screen = pygame.display.set_mode((width,height)) 
global select
select = 0
def notwise():
    global select
    select = not select
    return select
cell_area = [[0 for j in range(total)] for i in range(total)] #set still life, oscollator and spaceship in display cell
cell_area[50][50] = 1
cell_area[49][49] = 1
cell_area[49][50] = 1
cell_area[50][49] = 1

cell_area[60][60]=1
cell_area[61][60]=1
cell_area[60][61]=1
cell_area[61][62]=1
cell_area[62][61]=1

cell_area[30][30]=1
cell_area[29][30]=1
cell_area[31][30]=1

cell_area[10][10]=1
cell_area[11][10]=1
cell_area[12][10]=1
cell_area[10][11]=1
cell_area[9][11]=1
cell_area[11][11]=1

cell_area[71][68]=1
cell_area[70][70]=1
cell_area[71][70]=1
cell_area[72][70]=1
cell_area[72][69]=1

def display(total_range):   #draw cell
    for start_x in range(0,width,per_width):
        i = int(start_x / per_width)
        for start_y in range(0,height,per_height):
            j = int(start_y / per_height)
            if total_range[i][j] == 1 :
                pygame.draw.rect(screen,BLACK,(start_x,start_y,per_width,per_height),0)

def compute(total_range):           #select range
    row,column = numpy.shape(total_range)
    next_born = [[0 for j in range(row)] for i in range(column)]

    for i in range(row): # set loop where cell lives or die
        for j in range(column):
            if ((i-1) >=0 ) and ((j-1) >=0) and ((i+1) <= (row-1)) and ((j+1) <= (column-1)): # set range for cell
                live_neighbor = 0
                if total_range[i-1][j-1] ==1:
                    live_neighbor += 1
                if total_range[i][j-1] ==1:
                    live_neighbor += 1
                if total_range[i+1][j-1] ==1:
                    live_neighbor += 1
                if total_range[i-1][j] ==1:
                    live_neighbor += 1
                if total_range[i+1][j] ==1:
                    live_neighbor += 1
                if total_range[i-1][j+1] ==1:
                    live_neighbor += 1
                if total_range[i][j+1] ==1:
                    live_neighbor += 1
                if total_range[i+1][j+1] ==1:
                    live_neighbor += 1
            
                if total_range[i][j] != 0: #born cell
                    if (live_neighbor >=2) and (live_neighbor <=3 ):
                        next_born[i][j] = 1
                else:
                    if (live_neighbor ==3):
                        next_born[i][j] = 1
    return next_born                   

current_population = cell_area  #display area of cell
while True: #game event
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(WHITE)
    start = time.time() #calculate processing time
    display(current_population)
    pygame.display.update() #display update
    time.sleep(0.001) #set time to display
    screen.fill(WHITE)
    current_population = compute(current_population)
    display(current_population)
    pygame.display.update() #pygame update
    time.sleep(0.5)

