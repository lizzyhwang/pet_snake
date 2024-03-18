# Example file showing a basic pygame "game loop"
import pygame
from snake import Snake
from pygame import mixer

# pygame setup
pygame.init()

mWindowSize = 720
screen = pygame.display.set_mode((mWindowSize, mWindowSize))
clock = pygame.time.Clock()
running = True
mTileSize = 40
mSnake = Snake(mTileSize, mWindowSize)
headColor = (255,62,184)
bodyColor = (0,0,0)

mixer.init()
mixer.music.load("flight_of_bumblebees_8bit.wav") # .wav required, bugs with .mp3
mixer.music.set_volume(1.0)
mixer.music.play(-1) # -1 makes the music loop indefinitely

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    mSnake.addHead()
    for s in mSnake.body[1:]:
        pygame.draw.rect(screen, bodyColor, pygame.Rect(s[0]*mTileSize, s[1]*mTileSize, mTileSize, mTileSize))
    head = mSnake.getHead()
    pygame.draw.rect(screen,headColor,pygame.Rect(head[0]*mTileSize, head[1]*mTileSize, mTileSize, mTileSize))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 2

mixer.music.stop()
pygame.quit()