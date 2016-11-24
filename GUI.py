from Queue import Queue
import pygame

class GUI:
    def __init__(self, height, width):
        self.data = Queue()
        self.height = height
        self.width = width
        self.grid = [[0 for x in range(self.height)] for y in range(self.width)]
        self.images = []
        self.playersIM = []
        self.playername = "p0"
        pygame.init()
        self.WINDOW_SIZE = [320, 320]
        self.WIDTH = 32
        self.HEIGHT = 32
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("Tank Game")
        self.loadlandimages()
        self.loadlandimages()

    def loadplayerimages(self):
        for i in range(3):
            self.playersIM.append(pygame.image.load('Images/p'+i+1+'.png').convert())

    def loadlandimages(self):
        self.images.append(pygame.image.load('Images/brick.png').convert())
        self.images.append(pygame.image.load('Images/stone.png').convert())
        self.images.append(pygame.image.load('Images/water.png').convert())

    def initGUI(self, playerName, brick_coordinates, stone_coordinates, water_coordinates):
        for x,y in brick_coordinates:
            print x,y
            self.grid[x][y] = 1

        for x,y in stone_coordinates:
            print x,y
            self.grid[x][y] = 2

        for x,y in water_coordinates:
            print x,y
            self.grid[x][y] = 3

        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == 0:
                    color = (255, 255, 255)
                    pygame.draw.rect(self.screen,
                                     color,
                                     [self.WIDTH * i,
                                      self.HEIGHT * j,
                                      self.WIDTH,
                                      self.HEIGHT])
                elif self.grid[i][j] == 1:
                    self.screen.blit(self.images[0],(self.WIDTH * i,
                                      self.HEIGHT * j))
                elif self.grid[i][j] == 2:
                    self.screen.blit(self.images[1],(self.WIDTH * i,
                                      self.HEIGHT * j))
                elif self.grid[i][j] == 3:
                    self.screen.blit(self.images[2],(self.WIDTH * i,
                                      self.HEIGHT * j))

        pygame.display.flip()

    def start(self,tanks):
        for tank in tanks:
            self.screen.blit(self.playersIM[eval(tank[2])],eval(tank[1]))
        pygame.display.flip()
    def update(self, data):
        self.data.put(data)
        print data