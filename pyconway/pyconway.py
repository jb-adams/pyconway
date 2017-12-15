import pygame

class PyConway:
    def __init__(self):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.GRAY = (127,127,127)
        self.WIDTH = 600
        self.HEIGHT = 600
        self.SIZE = (self.WIDTH,self.HEIGHT)

        self.run()

    def run(self):

        #define game grid
        self.ncols = 100
        self.nrows = 100
        #define width and height of each 'cell' or box in the conway game
        self.cellwidth = self.WIDTH / self.ncols
        self.cellheight = self.HEIGHT / self.nrows
        #start pygame, set display mode and create clock object
        pygame.init()
        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()

        #create the starting, empty grid (all 0/off/white)
        self.oldgrid = self.get_starting_grid()
        self.newgrid = self.oldgrid

        pygame.display.set_caption("Jeremy's PyConway")

        in_progress = True
        game_started = False
        game_finished = False

        mousepos = None

        while in_progress:

            while not game_started:
                mousepos = pygame.mouse.get_pos()
                #print(pygame.key.get_pressed()[pygame.K_a])

                for event in pygame.event.get():
                    #print(event)
                    if event.type == pygame.QUIT:
                        in_progress = False
                        game_started = True
                        game_finished = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            #print("Game will now start")
                            game_started = True
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mousepos = pygame.mouse.get_pos()
                        #print(mousepos)

                        colidx_to_fill = int( mousepos[0]/self.cellwidth )
                        rowidx_to_fill = int( mousepos[1]/self.cellheight )

                        self.newgrid[rowidx_to_fill][colidx_to_fill] = 1

                self.clear_and_render_all()

            while not game_finished:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        in_progress = False
                        game_started = True
                        game_finished = True

                self.clear_and_render_all()

        pygame.quit()

    def get_starting_grid(self):
        D = {
            r : {c : 0 for c in range(0,self.ncols)}
            for r in range(0,self.nrows)
        }
        return D

    def evaluate_cell(self,state,neighbour_states_L):
        live_neighbours = 0
        dead_neighbours = 0

    def get_new_grid(self):
        pass

    def render_grid(self):

        #draw all horizontal lines to outline cells
        for rowidx in range(0,self.nrows):
            left = 0
            top = rowidx * self.cellheight
            rect = [left,top,self.WIDTH,1]
            pygame.draw.rect(self.screen,self.GRAY,rect,0)
        #draw all vertical lines to outline cells
        for colidx in range(0,self.ncols):
            left = colidx * self.cellwidth
            top = 0
            rect = [left,top,1,self.HEIGHT]
            pygame.draw.rect(self.screen,self.GRAY,rect,0)

    def render_cells(self):

        for rowidx in range(0,self.nrows):
            for colidx in range(0,self.ncols):
                on = self.newgrid[rowidx][colidx]
                if on:
                    left = colidx * self.cellwidth
                    top = rowidx * self.cellheight
                    rect = [left,top,self.cellwidth,self.cellheight]
                    pygame.draw.rect(self.screen,self.BLACK,rect,0)

    def clear_and_render_all(self):
        self.screen.fill(self.WHITE)
        self.render_grid()
        self.render_cells()
        pygame.display.flip()
        self.clock.tick(60)
