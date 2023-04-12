import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((0, 191, 255))
pygame.display.set_caption("Ülesanne 2")

pilt=pygame.image.load("bg.png")
ekraani_pind.blit(pilt,(0,0))
pygame.display.flip()

font=pygame.font.SysFont("Alganian",40)
sõnad="Nii ilus maja"
värv=[250, 0, 0]
teksti_lisanime=font.render(sõnad,False,värv)
ekraani_pind.blit(teksti_lisanime,(30,280))

pilt=pygame.image.load("stiv2.png")
ekraani_pind.blit(pilt,(20,310))
pygame.display.flip()




while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()
