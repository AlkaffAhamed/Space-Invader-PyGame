import pygame
import random
import math
from pygame import mixer

# Initialize the game
pygame.init()

# Create the screen (800x600)
screen = pygame.display.set_mode((800, 600))

# Title, background, icon and background music
pygame.display.set_caption("Space Invader PyGame")
icon = pygame.image.load("res/ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("res/background.png")
mixer.music.load("res/background.wav")
mixer.music.play(-1)

# Player
playerImg = pygame.image.load("res/player.png")
playerX, playerY = 370, 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6

for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load("res/enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Bullet
bulletImg = pygame.image.load("res/bullet.png")
bulletX, bulletY = 0, 480
bulletX_change, bulletY_change = 0, 10
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(x1, y1, x2, y2):
    dist = math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)
    dist = math.sqrt(dist)
    return dist < 27


score_value = 0
font = pygame.font.Font("freesansbold.ttf", 20)
textX, textY = 10, 10
gameover_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score():
    score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (textX, textY))


def gameover_text():
    gameover_tx = gameover_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameover_tx, (200, 250))


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
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("res/laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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
    # for loop to iterate through all the enemies
    for i in range(no_of_enemies):
        # Test for Game Over
        if enemyY[i] > 440:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            gameover_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

        # Collision Detection (moved inside the for loop)
        if isCollision(bulletX, bulletY, enemyX[i], enemyY[i]):
            explosion_sound = mixer.Sound("res/explosion.wav")
            explosion_sound.play()
            bulletY, bullet_state = 480, "ready"
            score_value += 1
            print(f"Score={score_value}")
            enemyX[i], enemyY[i] = random.randint(0, 735), random.randint(50, 150)

        # Draw the enemy moved inside for loop
        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY < 0:
        bulletY, bullet_state = 480, "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score()

    pygame.display.update()  # Very important line to display changes
