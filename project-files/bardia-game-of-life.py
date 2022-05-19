from turtle import color
import pygame , sys

pygame.init()


class Cell:


    def __init__(self , x ,  y , color):
        self.color = color
        self.rect = pygame.Rect(x , y , 9 , 9)


    def draw(self):

        pygame.draw.rect(main_screen , self.color, self.rect)

    def get_live_cells_around(self):
        res = 0
        x , y  = self.rect.x , self.rect.y

        #left pixel
        try:
            if main_screen.get_at((x - 2 , y)) == BLACK:
                res += 1
        except IndexError:
            pass
            
        #top pixel
        try:
            if main_screen.get_at((x , y - 2)) == BLACK:
                res += 1
        except IndexError:
            pass
        #right pixel
        try:
            if main_screen.get_at((x + 10 , y)) == BLACK:
                res += 1
        except IndexError:
            pass    
        #bottom pixel
        try:
            if main_screen.get_at((x , y + 10)) == BLACK:
                res += 1
        except IndexError:
            pass    
        #top_left pixel
        try:
            if main_screen.get_at((x - 2 , y - 2)) == BLACK:
                res += 1
        except IndexError:
            pass    
        #top_right pixel
        try:
            if main_screen.get_at((x + 10 , y - 2)) == BLACK:
                res += 1
        except IndexError:
            pass

        #bottom_left pixel

        try:
            if main_screen.get_at((x -2 , y + 10)) == BLACK:
                res += 1
        except IndexError:
            pass
        
        #bottom_right pixel
        try:
            if main_screen.get_at((x + 10 , y + 10)) == BLACK:
                res += 1
        except IndexError:
            pass

        return res



    @classmethod
    def draw_all_cells(cls , all_cells : list):

        for obj in all_cells:
            obj.draw()
    



BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)


all_cells = []


for x in range(1 , 1100 , 10):
    for y in range(1 , 700 , 10):

        all_cells.append(
            Cell(x , y , WHITE)
        )




main_screen = pygame.display.set_mode((1100 , 700))
pygame.display.set_caption("Conway's game of life")

def create_grid():

    for i in range(0 , 1101 , 10):
        pygame.draw.line(main_screen , BLACK , (i , 0 )  , (i , 700) , 1)

    for j in range(0 , 700 , 10):
        pygame.draw.line(main_screen , BLACK , (0 , j) , (1100 , j))

run = True
life = False

clock = pygame.time.Clock()

while run:
    clock.tick(70)
    if not life:
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    life = True
            
            mouse_pressed = pygame.mouse.get_pressed()

            if mouse_pressed[0] == True:
                pos = pygame.mouse.get_pos()

                x  = pos[0]
                y = pos[1]
                
                x = x//10  * 10 + 1
                y = y // 10 * 10 + 1
                pos = (x, y)

                for obj in range(len(all_cells)):
                    if all_cells[obj].rect.x == pos[0] and all_cells[obj].rect.y == pos[1]:
                        tmp = all_cells[obj]
                        tmp.color = BLACK
                        all_cells[obj] = tmp
                        break

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tmp = []
        for cell_i in range(len(all_cells)):
            
            cell = all_cells[cell_i]
            dummy = cell
            live_neighbors = cell.get_live_cells_around()
            if cell.color == BLACK:

                if live_neighbors < 2:
                    dummy.color = WHITE
                elif live_neighbors > 3:
                    dummy.color = WHITE

            elif cell.color == WHITE:

                if live_neighbors == 3:
                    dummy.color = BLACK
                

            tmp.append(dummy)

        
        all_cells = tmp.copy()



    main_screen.fill(WHITE)
    create_grid()

    Cell.draw_all_cells(all_cells)


    pygame.display.flip()
