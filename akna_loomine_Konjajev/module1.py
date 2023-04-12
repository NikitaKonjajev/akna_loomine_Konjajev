import pygame
import random 
import sys

def Maja(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y-((3/4.0)*kõrgus)), (x,y), (x+laius,y), (x+laius,y-(3/4.0)*(kõrgus)),(x,y-((3/4.0)*kõrgus)), (x+laius/2.0,y-kõrgus),(x+laius,y-(3/4.0)*kõrgus)]

    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,False,punktid,suurus)

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
fon=[r,g,b]

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
majavarv=[r,g,b]
pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Juhustikudobjektid")
pind.fill(fon) 

Maja(100,400,300,400,pind,majavarv)

ristkülik=pygame.Rect(120,217,80,80)
pygame.draw.rect(pind,(255, 255, 255),ristkülik)

for i in range(10):
    varv=[r,g,b]
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    #suurus
    laius=random.randint(1,80)
    kõrgus=random.randint(1,80)
    #asukoht
    x=random.randint(0,640-laius)
    y=random.randint(0,480-kõrgus)
    pygame.draw.rect(pind,varv,[x,y,laius,kõrgus])

    
    pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()




