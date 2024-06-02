import pygame

pygame.init()
screen_height = 300
screen_width = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')
grid = (0,0,0)
game = [[0,0,0],[0,0,0],[0,0,0]]
turn = 1

o_img = pygame.image.load('images/o_img.png')
o_img = pygame.transform.scale(o_img,(80,80))

x_img = pygame.image.load('images/x_img.jpg')
x_img = pygame.transform.scale(x_img, (80,80))
def draw_board():
    bg = (255,255,255)
    screen.fill(bg)
    for x in range(100,300,100):
        pygame.draw.line(screen, grid,(x,0),(x,300),5)
    for y in range(100,300,100):
        pygame.draw.line(screen, grid,(0,y),(300,y),5)


def draw_gamestate(gamestate):
    for i in range(3):
        for j in range(3):
            if gamestate[i][j] == 1:
                pygame.draw.circle(screen, grid,((j*100)+50,(i*100)+50),5)
                screen.blit(o_img, ((j*100)+10,(i*100)+10))
            if gamestate[i][j] == -1:
                pygame.draw.circle(screen, (0,0,200), ((j * 100) + 50, (i * 100) + 50),5)
                screen.blit(x_img, ((j * 100)+10, (i * 100)+10))

def end_game(game):
    for i in range (3):
        if game[i][0] == game[i][1] == game[i][2]:
            if game[i][0] != 0:
                return True
        if game[0][i] == game[1][i] == game[2][i]:
            if game[0][i] != 0:
                return True
    if game[0][0] == game[1][1] == game[2][2]:
        if game[0][0] != 0:
            return True
    if game[0][2] == game[1][1] == game[2][0]:
        if game[0][2] != 0:
            return True
    taken = 0
    for row in game:
        for column in row:
            if column != 0:
                taken+=1
    if taken == 9:
        return True
    return False


run = True
while run:
    draw_board()
    draw_gamestate(game)
    endgame = end_game(game)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if endgame == False:
                x,y = pygame.mouse.get_pos()
                if game[y//100][x//100] == 0:
                    game[y//100][x//100] = turn
                    turn *= -1
            if endgame == True:
                game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
