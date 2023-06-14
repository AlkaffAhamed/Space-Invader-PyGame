import pygame

# Initialize the game
pygame.init()

# Create the screen (800x600)
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invader PyGame")
icon = pygame.image.load("res/ufo.png")
pygame.display.set_icon(icon)

# Game Loop with Quit event
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
