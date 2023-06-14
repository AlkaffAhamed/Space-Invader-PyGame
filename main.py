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

    # Change background colour (RGB values)
    screen.fill((255, 255, 0))
    screen.fill((255, 0, 0), (20, 20, 40, 40))
    pygame.display.update()  # Very important line to display changes
