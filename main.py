import pygame
import random

# Initialize the game
pygame.init()

# Create the screen (800x600)
screen = pygame.display.set_mode((800, 600))

# Title, background and icon
pygame.display.set_caption("Space Invader PyGame")
icon = pygame.image.load("res/ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("res/background.png")

# Player
playerImg = pygame.image.load("res/player.png")
playerX, playerY = 370, 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg = pygame.image.load("res/enemy.png")
enemyX, enemyY = random.randint(0, 800), random.randint(50, 150)
enemyX_change, enemyY_change = 3, 40


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet
bulletImg = pygame.image.load("res/bullet.png")
bulletX, bulletY = 0, 480
bulletX_change, bulletY_change = 0, 10
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop with Quit event
running = True
while running:
    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # Bounding for spaceship
    # Spaceship is 64 px and width is 800 px
    # width - spaceship -> 800 - 64 = 736
    # 0 < playerX < 736
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    # Enemy movement
    # 0 < enemyX < 736
    # Once boundary is hit, enemy moves down by 40 px
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change

    # Bullet movement
    if bulletY < 0:
        bulletY, bullet_state = 480, "ready"
    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()  # Very important line to display changes
