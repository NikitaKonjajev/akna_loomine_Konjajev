﻿import pygame, random
while True:
        print("1 - legko")
        print("2 - bolee-menee")
        print("3 - ti ne potynesh")
        valik= int(input("Vali keerukus: "))
        if valik==1:
            pygame.init()
            green = [0, 255, 0]
            lBlue = [153, 204, 255]

            screenX = 640
            screenY = 480
            screen=pygame.display.set_mode([screenX, screenY])
            pygame.display.set_caption("pingpong")
            screen.fill(lBlue)
            clock=pygame.time.Clock()
            posX,posY=0,0
            speedX,speedY=2,2
            # задаем начальное положение и скорость для ristkülik1
            ristkülik1_x, ristkülik1_y = 230, 470
            ristkülik1_speed = 30
            # задаем начальное положение и скорость для ristkülik2
            ristkülik2_x, ristkülik2_y = 230, 5
            ristkülik2_speed = 30

            # чтобы выводился счет
            font = pygame.font.Font(None, 36)

            #мячик/игрок
            playerImage = pygame.image.load("sarik3.png")

            #мачик/игрок и очки
            enemies = []
            enemyImage = pygame.image.load('sarik3.png')
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
                        if event.key==pygame.K_LEFT:
                            ristkülik1_x -= ristkülik1_speed
                        elif event.key==pygame.K_RIGHT:
                            ristkülik1_x += ristkülik1_speed
                        elif event.key==pygame.K_a:
                            ristkülik2_x -= ristkülik2_speed
                        elif event.key==pygame.K_d:
                            ristkülik2_x += ristkülik2_speed
                # двигаем ristkülik1 влево или вправо
                if ristkülik1_x < 0:
                    ristkülik1_x = 0 # останавливаем ristkülik1 на левом краю экрана
                elif ristkülik1_x + 180 > screenX:
                    ristkülik1_x = screenX - 180 # останавливаем ristkülik1 на правом краю экрана

                # двигаем ristkülik2 влево или вправо
                if ristkülik2_x < 0:
                    ristkülik2_x = 0 # останавливаем ristkülik2 на левом краю экрана
                elif ristkülik2_x + 180 > screenX:
                    ristkülik2_x = screenX - 180 # останавливаем ristkülik2 на правом

                # вывод счета на экран
                scoreText = font.render("Ваш счет " + str(score), True, green)
                screen.blit(scoreText, (10, 10))

                #низ борт
                ristkülik1=pygame.Rect(ristkülik1_x, ristkülik1_y, 180, 7)
                pygame.draw.rect(screen,(0,0,0),ristkülik1)

                #вверхний борт
                ristkülik2=pygame.Rect(ristkülik2_x, ristkülik2_y, 180, 7)
                pygame.draw.rect(screen,(0,0,0),ristkülik2)

                player = pygame.Rect(posX, posY, 120, 140)
                screen.blit(playerImage, player)

                # collision detection logic for ristkülik1
                if player.colliderect(ristkülik1):
                    if speedY > 0:
                        posY = ristkülik1.top - player.height

                # проверка на очки
                if posX > screenX - playerImage.get_rect().width or posX < 0:
                    speedX = -speedX
                    if posY > 10 and posY < 110:
                        score += 1
                    print(score)

                if posY > screenY - playerImage.get_rect().height or posY < 0:
                    speedY = -speedY
                    if posX > 230 and posX < 410:
                        score += 1
                    print(score)

                # чтобы мячик катался
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
