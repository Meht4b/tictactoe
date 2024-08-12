import pygame
pygame.init()



gameGrid = [0,0,0,0,0,0,0,0,0]

def drawX(win,coords:tuple,size:int) -> None:

    pygame.draw.line(win,(255,255,255),(coords[0]-(size/2),coords[1]-(size/2)),(coords[0]+(size/2),coords[1]+(size/2)))
    pygame.draw.line(win,(255,255,255),(coords[0]-(size/2),coords[1]+(size/2)),(coords[0]+(size/2),coords[1]-(size/2)))

def drawO(win,coords:tuple,size:int)->None:
    pygame.draw.circle(win,(255,255,255),coords,size/2,width=1)

def drawGrid(win,grid:tuple,size:int,offsetX:int,offsetY:int) -> None:

    offsetX += size/2
    offsetY += size/2

    gap = size

    pygame.draw.line(win,(255,255,255),(offsetX-(size/2),offsetY-(size/2)+1.5*gap),(offsetX+3*size+1.5*gap,offsetY-(size/2)+1.5*gap))
    pygame.draw.line(win,(255,255,255),(offsetX-(size/2),offsetY-(size/2)+size+2.5*gap),(offsetX+3*size+1.5*gap,offsetY-(size/2)+size+2.5*gap))

    pygame.draw.line(win,(255,255,255),(offsetX-(size/2)+1.5*gap,offsetY-(size/2)),(offsetX-(size/2)+1.5*gap,offsetY+3*size+1.5*gap))
    pygame.draw.line(win,(255,255,255),(offsetX-(size/2)+size+2.5*gap,offsetY-(size/2)),(offsetX-(size/2)+size+2.5*gap,offsetY+3*size+1.5*gap))

    

    for i in range(len(gameGrid)):
        x = i%3
        y = i//3
        if gameGrid[i] == 1:
            drawX(win,(x*size+offsetX+gap*x,y*size+offsetY+gap*y),size)
        elif gameGrid[i] == 2:
            drawO(win,(x*size+offsetX+gap*x,y*size+offsetY+gap*y),size)

turn = 1

offsetX =50
offsetY = 50
size = 100


window = pygame.display.set_mode((offsetX*2+size*3+size*2,offsetY*2+size*3+size*2))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x = int((mouse_pos[0]-offsetX)//(size+size/2))
            y = int((mouse_pos[1]-offsetY)//(size+size/2))
            if x>2:
                x = 2
            if y >2:
                y = 2
            if x<0:
                x = 0
            if y <0:
                y = 0
            
            index =   x+(3*y)          

            if not gameGrid[index]:
                gameGrid[index] = turn

                if turn == 1:
                    turn = 2
                else:
                    turn = 1
        
            
    window.fill((0,0,0))
    drawGrid(window,gameGrid,size,offsetX,offsetY)

    pygame.display.update()