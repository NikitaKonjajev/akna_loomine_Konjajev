import pygame,sys 

pygame.init()
kollane=[255,255,10]
punane=[255,0,0]
hall=[200,200,200]
roosa=[255,150,255]
roheline=[100,255,100]

#ekraani suurus 
X=640
Y=480
ekraan=pygame.display.set_mode([X,Y])
pygame.display.set_caption("Animeerimine")
ekraan.fill(roheline)
kell=pygame.time.Clock()
mesilane=pygame.image.load("stiv2.png")
posX=X-mesilane.get_rect().width
posY=Y-mesilane.get_rect().height
lõpp=False 
sammX=2
sammY=0
samm=2
while not lõpp:
    kell.tick(60)
    event=pygame.event.get()
    for i in pygame.event.get():
        if i.type==pygame.QUIT():
            sys.exit()
    
    if posX>X-mesilane.get_rect().width or posX<0:
        sammX=-sammX
    if posY>Y-mesilane.get_rect().height or posY<0:
        sammY=-sammY

    if posX<0:
        sammY=2
        sammX=0

    if posY<0:
        sammY=0
        sammX=-2

    if posX<0:
        sammY=+2
        sammX=0





    posX-=sammX
    posY-=sammY




    ekraan.blit(mesilane,(posX,posY))
    pygame.display.flip()
    ekraan.fill(roheline)
pygame.quit()