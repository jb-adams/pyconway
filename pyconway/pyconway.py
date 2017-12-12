import pygame

class PyConway:
    def __init__(self):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.WIDTH = 600
        self.HEIGHT = 600
        self.SIZE = (self.WIDTH,self.HEIGHT)

        self.run()

    def run(self):

        #define game grid
        self.ncols = 100
        self.nrows = 100

        self.cellwidth = self.WIDTH / self.ncols
        self.cellheight = self.HEIGHT / self.nrows

        pygame.init()
        #self.screen = pygame.display.set_mode()
        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Jeremy's PyConway")

        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("User asked to quit.")
                    done = True
                elif event.type == pygame.KEYDOWN:
                    print("User pressed down on keyboard.")
                elif event.type == pygame.KEYUP:
                    print("User pressed up on keyboard.")
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("User clicked mouse button")

            self.screen.fill(self.WHITE)

            #drawing
            pygame.draw.rect(self.screen,self.BLACK,[50,50,200,200],0)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
