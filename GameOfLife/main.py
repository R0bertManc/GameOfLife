import numpy as np
import pygame
import time

size = width, height = 500, 500
cell_size = 10

nx_cells = (int)(width / cell_size)
ny_cells = (int)(height / cell_size)

cells = np.zeros((nx_cells,ny_cells))


#spaceship
cells [10][10] = 1
cells [13][10] = 1
cells [10][12] = 1
cells [11][13] = 1
cells [12][13] = 1
cells [13][13] = 1
cells [14][13] = 1
cells [14][12] = 1
cells [14][11] = 1

pygame.init()

pygame.display.set_caption("Game of Life")

screen = pygame.display.set_mode(size)
bg = 0, 0, 0
color = 200, 200, 200
screen.fill(bg)

pause = False

new_cells = np.copy(cells)

while 1:

    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pause = not pause

        mouse_clicks = pygame.mouse.get_pressed()

        if(sum(mouse_clicks) > 0):
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = (int) (mouse_pos[0]/cell_size)
            mouse_y = (int) (mouse_pos[1]/cell_size)
            new_cells[mouse_x, mouse_y] = not mouse_clicks[2]

        for y in range(nx_cells):
           for x in range(ny_cells):

               # draw cells
               if(cells[x,y] == 1):
                    pygame.draw.rect(screen,(220, 220, 220),(x*cell_size,y*cell_size,cell_size,cell_size))
               elif(cells[x,y] == 0):
                    pygame.draw.rect(screen, (20,20,20), (x * cell_size, y * cell_size, cell_size, cell_size))


               if (not pause):
                    #neighbours from each cell
                    neighbours = cells[(x-1) % nx_cells,(y-1) % ny_cells] \
                                 + cells[(x-1) % nx_cells, y] \
                                 + cells[x, (y-1) % ny_cells] \
                                 + cells[(x+1) % nx_cells, (y+1) % ny_cells] \
                                 + cells[x, (y+1) % ny_cells] \
                                 + cells[(x+1) % nx_cells,y] \
                                 + cells[(x-1) % nx_cells, (y+1) % ny_cells] \
                                 + cells[(x+1) % nx_cells, (y-1) % ny_cells]
           #conway's rules
                    if(cells[x,y] == 1 and (neighbours == 2 or neighbours == 3)):
                        new_cells[x,y] = 1
                    else:
                        new_cells[x,y] = 0
                    if (cells[x, y] == 0 and neighbours == 3):
                        new_cells[x, y] = 1


        #draw grid
        for i in range(ny_cells):
            for j in range(nx_cells):
                pygame.draw.rect(screen, (220, 220, 220), (j * cell_size, i * cell_size, cell_size, cell_size), 1)

        cells = np.copy(new_cells)

        pygame.display.flip()
        time.sleep(0.1)
