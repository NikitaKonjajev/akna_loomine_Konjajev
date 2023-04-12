import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((0, 191, 255))
pygame.display.set_caption("Esimene aken")

ristkülik=pygame.Rect(0,300,640,180)
pygame.draw.rect(ekraani_pind,(0, 255, 0),ristkülik)

ristkülik=pygame.Rect(50,217,230,150)
pygame.draw.rect(ekraani_pind,(139, 69, 19),ristkülik)

jalg=pygame.Rect(490,200,30,200)
pygame.draw.rect(ekraani_pind,(139, 69, 19),jalg)

ristkülik=pygame.Rect(450,200,110,130)
pygame.draw.rect(ekraani_pind,(0, 128, 0),ristkülik)

ristkülik=pygame.Rect(80,260,50,50)
pygame.draw.rect(ekraani_pind,(255,255,255),ristkülik)

pilt=pygame.image.load("stiv2.png")
ekraani_pind.blit(pilt,(330,290))

font=pygame.font.SysFont("Alganian",40)
sõnad="Где мои алмазы??"
värv=[0, 0, 0]
teksti_lisanime=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisanime,(50,50))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()


369,227,563,303




"""
ristkülik=pygame.Rect(0,0,100,100)
pygame.draw.rect(ekraani_pind,(0, 255, 0),ristkülik)

ristkülik=pygame.Rect(180,80,175,175)
pygame.draw.rect(ekraani_pind,(0, 255, 255),ristkülik)

ristkülik=pygame.Rect(200,300,400,175)
pygame.draw.rect(ekraani_pind,(255, 255, 0),ristkülik)

ristkülik=pygame.Rect(200,300,400,175)
pygame.draw.rect(ekraani_pind,(255, 255, 0),ristkülik)
"""
"""
joon (line): pygame.draw.line(aken, värv, algus_pos, lõpp_pos, paksus)
ristkülik (rect): pygame.draw.rect(screen, värv, [x, y, w, h], joone_paksus)
ring (circle): pygame.draw.circle(screen, värv, tsentri_pos, raadius, joone_paksus)
hulknurk (polygon): pygame.draw.polygon(screen, värv, koordinaatide_loend, joone_paksus)
ovaal (ellipse): pygame.draw.ellipse(screen, värv, [x, y, r1, r2], joone_paksus)
kaar (arc): pygame.draw.arc(screen, värv, ristküliku_koordinaadid, start_nurk, lõpp_nurk, joone_paksus)
jalg=pygame.Rect(66,50,5,500)
pygame.draw.rect(ekraani_pind,(0, 0, 0),jalg)
"""