import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("space invader")
icon = pygame.image.load("4th-of-july.png")
pygame.display.set_icon(icon)

# adding background image
backgroundimg = pygame.image.load("space-background.png")

# adding player image
playerimg = pygame.image.load("space-shuttle.png")
playerX = 370
playerY = 480
playerX_change = 0

# adding bullet image
bulletimg = pygame.image.load("space-bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 30
bullet_state = "ready"

enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10

# adding enemy image
for i in range(no_of_enemies):
    enemyimg.append(pygame.image.load("space-enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textY = 10
textX = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def firebullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


def isollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundimg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    firebullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    # player movement
    playerX += playerX_change

    if playerX >= 745:
        playerX = 745
    elif playerX <= -9:
        playerX = -9

    # enemy movement
    for i in range(no_of_enemies):
        if enemyY[i] > 440:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] >= 745:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] <= -9:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
        # iscollision
        collision = isollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        firebullet(bulletX, bulletY)
        bulletY -= bulletY_change

    show_score(textX, textY)
    player(playerX, playerY)
    pygame.display.update()
