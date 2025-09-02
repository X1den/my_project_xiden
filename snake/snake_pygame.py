import pygame 

pygame.init()
dis = pygame.display.set_mode((600,600))

pygame.display.update()

snake = [(20,20)]
direction = "stop"
CELL_SIZE = 20

pygame.quit()
quit()