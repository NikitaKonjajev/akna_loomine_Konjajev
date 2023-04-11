import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((300,300))
ekraani_pind.fill((0, 191, 255))
pygame.display.set_caption("Lumemees - Nikita Konjajev")


#шары
lill=pygame.Rect(110,178,100,100)
pygame.draw.ellipse(ekraani_pind,(255,255,255),lill)
lill=pygame.Rect(118,110,75,75)
pygame.draw.ellipse(ekraani_pind,(255,255,255),lill)
lill=pygame.Rect(129,63,50,50)
pygame.draw.ellipse(ekraani_pind,(255,255,255),lill)

#глаза
lill=pygame.Rect(140,80,5,5)
pygame.draw.ellipse(ekraani_pind,(255, 0, 0),lill)
lill=pygame.Rect(160,80,5,5)
pygame.draw.ellipse(ekraani_pind,(255, 0, 0),lill)

#пуговицы 2
lill=pygame.Rect(148,130,12,12)
pygame.draw.ellipse(ekraani_pind,(0,0,0),lill)
lill=pygame.Rect(148,150,12,12)
pygame.draw.ellipse(ekraani_pind,(0,0,0),lill)

#пуговицы 3
lill=pygame.Rect(152,200,12,12)
pygame.draw.ellipse(ekraani_pind,(0,0,0),lill)
lill=pygame.Rect(152,220,12,12)
pygame.draw.ellipse(ekraani_pind,(0,0,0),lill)
lill=pygame.Rect(152,240,12,12)
pygame.draw.ellipse(ekraani_pind,(0,0,0),lill)

#нос
pygame.draw.polygon(ekraani_pind,(255, 69, 0),[(151, 89), (146, 100), (158, 100)])

#руки
lill=pygame.Rect(95,130,25,25)
pygame.draw.ellipse(ekraani_pind,(255, 255, 255),lill)
lill=pygame.Rect(190,130,25,25)
pygame.draw.ellipse(ekraani_pind,(255, 255, 255),lill)
#ноги
lill=pygame.Rect(110,260,30,30)
pygame.draw.ellipse(ekraani_pind,(255,255,255),lill)
lill=pygame.Rect(180,260,30,30)
pygame.draw.ellipse(ekraani_pind,(255,255,255),lill)

#шляпа
lill=pygame.Rect(120, 45, 70, 20)
pygame.draw.rect(ekraani_pind, (139, 69, 19),lill)

pilt=pygame.image.load("сон5.png")
ekraani_pind.blit(pilt,(20,20))
pygame.display.flip()

font=pygame.font.SysFont("Alganian",15)
sõnad="А где снег?"
värv=[0,0,0]
teksti_lisanime=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisanime,(50,25))

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()