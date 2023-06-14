import pygame

# Initialize the game
pygame.init()

# Create the screen (800x600)
screen = pygame.display.set_mode((800, 600))

# Game Loop with Quit event
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
