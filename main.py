import pygame

# Initialize the game
pygame.init()

# Create the screen (800x600)
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invader PyGame")
icon = pygame.image.load("res/ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("res/player.png")
playerX, playerY = 370, 480


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop with Quit event
running = True
while running:
    # Black background colour (RGB values)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke events
        if event.type == pygame.KEYDOWN:
            print("Key pressed")
            if event.key == pygame.K_LEFT:
                print("Left key pressed!")
            if event.key == pygame.K_RIGHT:
                print("Right key pressed!")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key released!")
            else:
                print("Random Key released!")

    player(playerX, playerY)
    pygame.display.update()  # Very important line to display changes
