from Queue import Queue
import pygame
from threading import Timer


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
        self.loadplayerimages()
        self.player_positions = []
        self.player_positions_2 = []

    def loadplayerimages(self):
        for i in range(5):
            self.playersIM.append(pygame.image.load('Images/p' + str(i + 1) + '.png').convert())
        print self.playersIM

    def loadlandimages(self):
        self.images.append(pygame.image.load('Images/brick.png').convert())
        self.images.append(pygame.image.load('Images/stone.png').convert())
        self.images.append(pygame.image.load('Images/water.png').convert())
        self.images.append(pygame.image.load('Images/coin.png').convert())
        self.images.append(pygame.image.load('Images/life.png').convert())

    def initGUI(self, brick_coordinates, stone_coordinates, water_coordinates):
        for x, y in brick_coordinates:
            self.grid[x][y] = 1

        for x, y in stone_coordinates:
            self.grid[x][y] = 2

        for x, y in water_coordinates:
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
                    self.screen.blit(self.images[0], (self.WIDTH * i,
                                                      self.HEIGHT * j))
                elif self.grid[i][j] == 2:
                    self.screen.blit(self.images[1], (self.WIDTH * i,
                                                      self.HEIGHT * j))
                elif self.grid[i][j] == 3:
                    self.screen.blit(self.images[2], (self.WIDTH * i,
                                                      self.HEIGHT * j))

        pygame.display.flip()

    def start(self, tanks):
        self.player_positions = tanks
        for tank in tanks:
            print tank, eval(tank[2]), eval(tank[1])
            self.screen.blit(self.playersIM[eval(tank[0][1])],
                             (self.WIDTH * eval(tank[1]), self.HEIGHT * eval(tank[2])))
        pygame.display.flip()

    def update(self, data):
        # self.data.put(data)
        print data

    def updatePlayers(self,player_info):

        if self.data.empty():
            for tank in self.player_positions:
                color = (255, 255, 255)
                pygame.draw.rect(self.screen,
                                 color,
                                 [self.WIDTH * eval(tank[1]),
                                  self.HEIGHT * eval(tank[2]),
                                  self.WIDTH,
                                  self.HEIGHT])
        else:
            for i in range(len(self.player_positions_2)):
                color = (255, 255, 255)
                pygame.draw.rect(self.screen,
                                 color,
                                 [self.WIDTH * self.player_positions_2[i][0][0],
                                  self.HEIGHT * self.player_positions_2[i][0][1],
                                  self.WIDTH,
                                  self.HEIGHT])

        self.data.put(player_info)
        for i in range(len(player_info)):
            im = pygame.transform.rotate(self.playersIM[i], -90 * player_info[i][1])
            self.screen.blit(im,
                             (self.WIDTH * player_info[i][0][0], self.HEIGHT * player_info[i][0][1]))
        pygame.display.flip()
        self.player_positions_2 = player_info

    def addCoin(self, coin):
        self.screen.blit(self.images[3], (self.WIDTH * coin[0][0], self.HEIGHT * coin[0][1]))
        pygame.display.flip()

        def disappear(self, coin):
            color = (255, 255, 255)
            pygame.draw.rect(self.screen,
                             color,
                             [self.WIDTH * coin[0][0],
                              self.HEIGHT * coin[0][1],
                              self.WIDTH,
                              self.HEIGHT])
            pygame.display.flip()

        Timer(float(coin[1])/1000, disappear, [self, coin]).start()

    def addLife(self, life):
        self.screen.blit(self.images[4], (self.WIDTH * life[0][0], self.HEIGHT * life[0][1]))
        pygame.display.flip()

        def disappear(self, life):
            color = (255, 255, 255)
            pygame.draw.rect(self.screen,
                             color,
                             [self.WIDTH * life[0][0],
                              self.HEIGHT * life[0][1],
                              self.WIDTH,
                              self.HEIGHT])
            pygame.display.flip()
        Timer(float(life[1])/1000, disappear, [self,life]).start()
