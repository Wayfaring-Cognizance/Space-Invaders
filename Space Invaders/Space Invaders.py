import pygame
from pygame import mixer

import random
import math

#It needs this to work, it initializes Pygame
pygame.init()

#Create Screen
screen = pygame.display.set_mode((1000, 800))

#Background
#background = pygame.image.load(r'') Didn't find one I liked. The black is like space.

#Background Sound
mixer.music.load(r'spaceinvaders1.mpeg')
mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(r'spaceship.png')#use 32X32 for pygame icons. Start with r
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load(r'ship.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(r'Alien.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40) #makes it go down after hiting the wall

#Bullet
bulletImg = pygame.image.load(r'C:\Users\kolson.BPWC-L17-7\Downloads\bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready" #this means you can't see the bullet. "fire" means its moving

#Score

score_value = 0
font = pygame.font.Font ('freesansbold.ttf', 32)

textX = 10
textY = 10

#Game Over Text
over_font = pygame.font.Font ('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (round(x),round(y)))

def game_over_text():
    over_text = over_font.render(("GAME OVER"), True, (255,255,255))
    screen.blit(over_text, (200, 250))
    
def player(x,y):
    screen.blit(playerImg, (round(x),round(y)))#means draw

def enemy(x, y, i):
    screen.blit(enemyImg[i], (round(x),round(y)))#weird error about float values if no round...

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(round(x + 16),round(y + 10))) #makes it appear wherever ship is
    
def isCollision(enemyX,enemyY,bulletX,bulletY): #uses math for Distance between two points and the midpoint
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#Game Loop
running = True
while running:

    screen.fill((0,0,0))#Red, Green, Blue. Google can show you how to do diff colors
    #Background Image
    # Got rid of bg because wasn't worth it. things get slow because it's too big screen.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #If keystroke is pressed, check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    #Bullet sound
                    bullet_sound = mixer.Sound(r'Flash-laser-03.wav')
                    bullet_sound.play()
                    bulletX = playerX #Gets the current x cordinate of the spaceship
                    fire_bullet(bulletX,bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            
    #Establishing boundaries for space ship
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: #this is because the ship is 64 pixels. 800-64=736
        playerX = 736

    #Enemy movement
    for i in range(num_of_enemies):

        #Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000 #moving all enemies away
            game_over_text()
            break
            
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound(r'Explosion+3.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
            
        enemy(enemyX[i], enemyY[i], i)

    #Bullet Movement
    if bulletY <= 0 :
        bulletY = 480
        bullet_state = "ready"
            
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
        
    player(playerX,playerY)
    show_score(textX, textY)
    pygame.display.update()#have to do this after each display update
    
