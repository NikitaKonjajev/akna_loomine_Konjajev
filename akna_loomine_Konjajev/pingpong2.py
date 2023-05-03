import pygame,sys
from turtle import pos
import random
        


def liik():
    global posX3,posY3,sammX3,sammY3
    if posX3>=screenX-playerImage.get_rect().width or posX3<0:  # Оталкивание от стеноки по оси X
        sammX3=-sammX3

    if posY3>=screenY-playerImage.get_rect().height or posY3<0:  # вверх/вниз после косания нижней границы
        sammY3=-sammY3

    posX3+=sammX3
    posY3+=sammY3

    screen.blit(playerImage,(posX3,posY3))
    pygame.display.flip()
    screen.fill(lblue)





pygame.init()

red=[255,0,0]
blue=[0,0,255]
lblue=[153,204,255]


screenX=640
screenY=480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Animatsion")
screen.fill(lblue)
clock=pygame.time.Clock()


posX,posY=screenX/2, screenY/2

posX2,posY2=screenX/2, screenY/2 #

posX3, posY3 = 0, 0 ##

sammX3,sammY3=2,2 ##


speedY=0


speedY2 =0 #

speedX3, speedY3 = 3, 3 ##

directionY=0 

directionY2= 0 #
player = pygame.Rect(posX3, posY3, 80, 40)
playerImage = pygame.image.load("sarik3.png")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])
posX3=screenX-playerImage.get_rect().width
posY3=screenY-playerImage.get_rect().height

enemies = []
enemyCounter = 0
totalenemies = 20
score = 0
gameover=False

while not gameover:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover=True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                directionY="move_up"
       
            elif event.key==pygame.K_DOWN:
                directionY="move_down"
                
        elif event.type==pygame.KEYUP:
             if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                 speedY=0

             if event.key==pygame.K_w or event.key==pygame.K_s:
                 speedY2=0
    if directionY=="move_up":
        if posY>0:
            posY-=3
    elif directionY=="move_down":
        if posY + 100 <screenY:
            posY+=3





    events=pygame.event.get()
    for i in pygame.event.get():
          sys.exit()
    liik()


    if posX3 > screenX - playerImage.get_rect().width or posX3 < 0:
        
        if posY3 > 150 and posY3 < 368:
            score += 1
        print(score)
    
    if posY3 > screenY - playerImage.get_rect().height or posY3 < 0:
      
        if posX3 > 150 and posX3 < 290:
            score += 1
        print(score)
    

    for enemy in enemies[:]:
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1
            print(score)


    ruut=pygame.draw.rect(screen,red,[610,posY,12,100],0,10)
    ruut2=pygame.draw.rect(screen,blue,[20,posY2,12,100],0,10)

print(score)
if score == 20:
    gameover = True



pygame.display.flip()
screen.fill(lblue)
pygame.quit
