import pygame, random
pygame.init()


red = [255, 0, 0]
green = [0, 255, 0]
blue = [6, 6, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("pingpong")
screen.fill(lBlue)
clock=pygame.time.Clock()
posX,posY=0,0
speedX,speedY=3,4

def my(score):
    value=screen.render("Vash s4et: "+str(score),True)dis.blit(value,[0,0])
#player
player = pygame.Rect(posX, posY, 120, 120)
playerImage = pygame.image.load("sarik3.png")

#enemy - tekitame 5 suvalist vaenlast
enemies = []
enemyImage = pygame.image.load('sarik3.png')
enemyCounter = 0
totalenemies = 20
score = 0
gameover=False
while not gameover:
    clock.tick(60)
    #mangu sulgemine ristist
    event = pygame.event.poll()
    if event.type==pygame.QUIT:
        break
    player = pygame.Rect(posX, posY, 120, 140)
    screen.blit(playerImage, player)
    
    #левый борт
    pilt=pygame.image.load("bortik1.png")
    screen.blit(pilt,(150,-80))
    
    #правый борт
    pilt=pygame.image.load("bortik1.png")
    screen.blit(pilt,(150,368))

    pygame.display.flip()

    # Check collision with borders
    if posX > screenX - playerImage.get_rect().width or posX < 0:
        speedX = -speedX
        if posY > 150 and posY < 368:
            score += 1
        print(score)
    
    if posY > screenY - playerImage.get_rect().height or posY < 0:
        speedY = -speedY
        if posX > 150 and posX < 290:
            score += 1
        print(score)

    # Update ball position
    posX += speedX
    posY += speedY

    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1
            print(score)

    pygame.display.flip()
    screen.fill(lBlue)

print(score)
if score == 20:
    gameover = True
pygame.quit()
