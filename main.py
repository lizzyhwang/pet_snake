# Example file showing a basic pygame "game loop"
import pygame
from snake import Snake

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
mSnake = Snake()
headColor = (255,62,184)
bodyColor = (0,0,0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    mSnake.addHead()
    for s in mSnake.body[1:]:
        pygame.draw.rect(screen, bodyColor, pygame.Rect(s[0]*40, s[1]*40, 40, 40))
    head = mSnake.getHead()
    pygame.draw.rect(screen,headColor,pygame.Rect(head[0]*40, head[1]*40, 40, 40))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 2

pygame.quit()