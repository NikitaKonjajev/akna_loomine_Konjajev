def anim(posX, posY, sammX, sammY, X, Y, mesilane): #сам код из кода Марины
    if posX == 0 and posY == 0:
        sammX = 1
        sammY = 0
    if posX == X - mesilane.get_rect().width and posY <= Y - mesilane.get_rect().height:
        sammX = 0
        sammY = 1
    if posX <= X - mesilane.get_rect().width and posY == Y - mesilane.get_rect().height:
        sammX = 1
        sammY = 0
        sammX = -sammX
    if posX == 0 and posY >= Y - mesilane.get_rect().height:
        sammX = 0
        sammY = 1
        sammY = -sammY
    posX += sammX
    posY += sammY
    return posX, posY, sammX, sammY


def anim2(posX, posY, sammX, sammY, X, Y, mesilane):
    posX -= sammX
    posY -= sammY
    if posX >= X - mesilane.get_rect().width or posX < 0:
        sammX = -sammX
    if posY >= Y - mesilane.get_rect().height or posY < 0:
        sammY = -sammY
    return posX, posY, sammX, sammY
