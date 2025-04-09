from pydoc import resolve
import pygame 
import sys
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
pathToVegeta = f'{BASE_PATH}' + '\images\\vegeta.jpg'


BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

ballImage = pygame.image.load(f'{pathToVegeta}')

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    window.fill(BLACK)
    window.blit(ballImage, (0,0))
    pygame.display.update()
    
    clock.tick(FRAMES_PER_SECOND)