import pygame

pygame.init()

sw = 800
sh = 600

board = pygame.image.load('imgs/board.jpg')
x_img = pygame.image.load('imgs/x.png')
o_img = pygame.image.load('imgs/o.png')

win = pygame.display.set_mode((sw, sh))

clock = pygame.time.Clock()

boardVals = [[0,0,0], [0,0,0], [0,0,0]]

piecesOnBoard = []

moveCount = 0

gameOver = False

class Piece(object):
    def __init__(self, x, y, isX):
        self.x = x
        self.y = y
        self.isX = isX
        self.xTrue = self.x - (self.x % 200)
        self.yTrue = self.y - (self.y % 200)
        if isX:
            self.image = x_img
        else:
            self.image = o_img

    def draw(self, win):

        win.blit(self.image, (self.xTrue, self.yTrue))


def redrawGameWindow():
    win.blit(board, (0,0))
    pygame.draw.rect(win, (0,0,0), [600, 0, 200, 600])

    for piece in piecesOnBoard:
        piece.draw(win)


    pygame.display.update()

def isGameOver():
    zeroFound = False
    for i in boardVals:
        for j in i:
            if j == 0:
                zeroFound = True
    if not zeroFound:
        return True

    # Horizonal Win
    for i in boardVals:
        if i[0] == i[1] and i[0] == i[2] and i[0] != 0:
            return True

    # Vertical Win
    if boardVals[0][0] == boardVals[1][0] and boardVals[0][0] == boardVals[2][0]:
        if boardVals[0][0] != 0:
            return True
    if boardVals[0][1] == boardVals[1][1] and boardVals[0][1] == boardVals[2][1]:
        if boardVals[0][1] != 0:
            return True
    if boardVals[0][2] == boardVals[1][2] and boardVals[0][2] == boardVals[2][2]:
        if boardVals[0][2] != 0:
            return True

    #Diagonal Check
    if boardVals[0][0] == boardVals[1][1] and boardVals[0][0] == boardVals[2][2]:
        if boardVals[0][0] != 0:
            return True

    if boardVals[0][2] == boardVals[1][1] and boardVals[0][2] == boardVals[2][0]:
        if boardVals[0][0] != 0:
            return True



run = True
while run:
    clock.tick(50)

    if not gameOver:
        mouseX, mouseY = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if click != (0,0,0):
            if moveCount % 2 == 0:
                if boardVals[mouseY//200][mouseX//200] == 0:
                    piecesOnBoard.append(Piece(mouseX, mouseY, True))
                    boardVals[mouseY//200][mouseX//200] = 1
                    moveCount += 1
            else:
                if boardVals[mouseY // 200][mouseX // 200] == 0:
                    piecesOnBoard.append(Piece(mouseX, mouseY, False))
                    boardVals[mouseY // 200][mouseX // 200] = -1
                    moveCount += 1

        gameOver = isGameOver()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()

pygame.quit()