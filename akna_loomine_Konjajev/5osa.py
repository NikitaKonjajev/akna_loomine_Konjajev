import pygame, random
pygame. init()

red = [255, 0, 0]
green = [0, 255, 0]
blue = [6, 6, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

screenX = 640
screenY = 480
screen=pygame.display. set_mode([screenX, screenY])
pygame.display.set_caption("surface")
screen.fill(lBlue)
clock=pygame.time.Clock()
posX,posY=0,0
speedX,speedY=3,4

#player
player = pygame.Rect(posX, posY, 120, 120)
playerImage = pygame.image.load("sarik3.png")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])

#enemy
enemy = pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73)
enemyImage = pygame.image.load("stiv2.png")
enemyImage = pygame.transform.scale(enemyImage, [enemy.width, enemy.height])

score = 0
gameover=False
while not gameover:
    clock.tick(60)
    #mangu sulgemine ristist
    event = pygame.event.poll()
    if event.type==pygame.QUIT:
        break
    #player Liikumine
    player = pygame.Rect(posX, posY, 120, 140)
    screen.blit(playerImage, player)

    posX+=speedX
    posY+=speedY

    if posX > screenX-playerImage.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > screenY-playerImage.get_rect().height or posY < 0:
        speedY = -speedY

    #enemy Liikumine ja puudutamine
    if player.colliderect(enemy):
        enemy.x = random.randint(0, screenX - enemy.width)
        enemy.y = random.randint(0, screenY - enemy.height)
        score += 1
        print(score)

    screen.blit(enemyImage,enemy)
    pygame.display.flip()
    screen.fill(lBlue)

print(score)
pygame.quit()