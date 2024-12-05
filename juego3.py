import pygame, time
pygame.init()
screen=pygame.display.set_mode((450,450))
pygame.display.set_caption("juego triki")
fondo, circulo, equis, reload, ganadorX, ganadorO = pygame.transform.scale(pygame.image.load("img/Tablero.png"),(450,450)), pygame.transform.scale(pygame.image.load("img/Circulo.png"),(125,125)), pygame.transform.scale(pygame.image.load("img/Equis.png"),(125,125)), pygame.transform.scale(pygame.image.load("img/Reload.png"),(50,50)), pygame.transform.scale(pygame.image.load("img/X.png"),(100,50)), pygame.transform.scale(pygame.image.load("img/O.png"),(100,50))
coordenadas, tablero =[[(40,50),(165,50),(290,50)], [(40,175),(165,175),(290,175)], [(40,300),(165,300),(290,300)]], [["","",""], ["","",""], ["","",""] ]
listadoX=[0, 1, 2]
triqui=False
turno="O"
game_over=False
reloj=pygame.time.Clock()
def graficartablero(ganador, perdedor):
    screen.blit(fondo,(0,0))
    screen.blit(reload,(0,0))
    if ganador:
        if perdedor == "X":
            screen.blit(ganadorO,(165,0))
        else:
            screen.blit(ganadorX,(165,0))
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna]=="O": graficar_O(fila,columna)
            elif tablero[fila][columna]=="X": graficar_X(fila,columna)
    pygame.display.flip()
def graficar_O(fila, columna): screen.blit(circulo,coordenadas[fila][columna])
def graficar_X(fila, columna): screen.blit(equis,coordenadas[fila][columna])
while not game_over:
    reloj.tick(30)
    graficartablero(triqui, turno)
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT: game_over=True
        elif evento.type==pygame.MOUSEBUTTONDOWN:
            mouseX,mouseY=evento.pos
            if(mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425):
                fila=(mouseY-50)//125; columna=(mouseX-40)//125
                if tablero[fila][columna]=="":
                    tablero[fila][columna]=turno
                    for a in listadoX:
                        if turno == tablero[0][a] and turno == tablero[1][a] and turno == tablero[2][a]: triqui=True
                        elif turno == tablero[a][0] and turno == tablero[a][1] and turno == tablero[a][2]: triqui=True
                        elif turno == tablero[0][0] and turno == tablero[1][1] and turno == tablero[2][2]: triqui=True
                        elif turno == tablero[0][2] and turno == tablero[1][1] and turno == tablero[2][0]: triqui=True
                    graficartablero(triqui, turno)
                    if triqui:
                        pygame.display.set_caption(f"¡{turno} ha ganado!")
                        time.sleep(13)
                        game_over = True
                    if turno=="O": turno="X"
                    else: turno="O"
            elif (mouseX >= 0 and mouseX < 50) and (mouseY >= 0 and mouseY < 50):
                tablero=[["","",""], ["","",""], ["","",""]]
                turno="O"
                triqui=False
                graficartablero(triqui, turno)
pygame.quit        
             