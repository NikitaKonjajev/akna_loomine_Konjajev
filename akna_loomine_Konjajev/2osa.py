import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((0, 191, 255))
pygame.display.set_caption("Ülesanne 2")




pilt=pygame.image.load("bg.png")
ekraani_pind.blit(pilt,(0,0))
pygame.display.flip()

pilt=pygame.image.load("stiv2.png")
ekraani_pind.blit(pilt,(20,310))
pygame.display.flip()

font=tekst=pygame.font.SysFont("Alganian",40)
sõnad="Где снег?"
värv=[0,0,0]
teksti_lisamine=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisamine,(150,10))

while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
