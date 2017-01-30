import heapq
from Queue import Queue

import collections

from Messenger import Messenger
from random import randint


class Brain:
    def __init__(self):
        self.data = Queue()
        self.MOVES = ["RIGHT#", "LEFT#", "UP#", "DOWN#", "SHOOT#"]
        self.player_name = 0
        self.brick_coordinates = []
        self.stone_coordinates = []
        self.water_coordinates = []
        self.coins = []
        self.position = [0, 0]
        self.tanks = []
        self.player_positions = []
        self.player_positions_2 = []
        self.paths = []
        self.current_path = []

    def initBrain(self, player_name, brick_coordinates, stone_coordinates, water_coordinates):
        self.player_name = player_name
        self.brick_coordinates = brick_coordinates
        self.stone_coordinates = stone_coordinates
        self.water_coordinates = water_coordinates

    def addCoin(self, coin):
        g = GridWithWeights(10, 10)
        g.walls = self.water_coordinates + self.stone_coordinates + self.brick_coordinates
        i = self.player_name
        if not self.player_positions:
            x, y = int(self.tanks[self.player_name][1]), int(self.tanks[self.player_name][2])
        else:
            x, y = int(self.player_positions[i][0][0]), int(self.player_positions[i][0][0])
        came_from, cost_so_far = dijkstra_search(g, (x, y), coin[0])
        path = reconstruct_path(came_from, start=(x, y), goal=coin[0])
        print path
        self.paths.append(path)

    def addLife(self, life):
        g = GridWithWeights(10, 10)
        g.walls = self.water_coordinates + self.stone_coordinates + self.brick_coordinates
        i = self.player_name
        if not self.player_positions:
            x, y = self.tanks[self.player_name][1], self.tanks[self.player_name][2]
        else:
            x, y = self.player_positions[i][0][0], self.player_positions[i][0][0]
        came_from, cost_so_far = dijkstra_search(g, (x, y), life[0])
        path = reconstruct_path(came_from, start=(x, y), goal=life[0])
        print path
        self.paths.append(path)

    def addtanks(self, tank):
        self.tanks = tank

    def update(self, data):
        self.player_positions = data
        self.decide(data)
        print data

    def decide(self, player_info):
        i = self.player_name
        if not self.current_path and self.paths:
            self.current_path = self.paths.pop()
            self.current_path.pop(0)
            self.current_path.pop(0)
            move = self.think_to_move((player_info[i][0][0], player_info[i][0][1]), self.current_path[0],
                                      player_info[i][1])
            print "other"
        elif self.current_path:
            move = self.think_to_move((player_info[i][0][0], player_info[i][0][1]), self.current_path[0], player_info[i][1])
            print "paths"
        else:
            move = "SHOOT#"
        print self.current_path
        Messenger().send(move, '192.168.8.101', 6000)

    def think_to_move(self, current_position, expected_position, direction):
        x_diff = current_position[0] - expected_position[0]
        y_diff = current_position[1] - expected_position[1]
        print "diff",x_diff,y_diff,direction,current_position,expected_position
        if not x_diff:
            if y_diff > 0:
                if direction == 0:
                    self.current_path.pop(0)
                    return "UP#"
                else:
                    return "UP#"
            elif y_diff < 0:
                if direction == 2:
                    self.current_path.pop(0)
                    return "DOWN#"
                else:
                    return "DOWN#"

        elif not y_diff:
            if x_diff > 0:
                if direction == 3:
                    self.current_path.pop(0)
                    return "LEFT#"
                else:
                    return "LEFT#"
            elif x_diff < 0:
                if direction == 1:
                    self.current_path.pop(0)
                    return "RIGHT#"
                else:
                    return "RIGHT#"


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0: results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


def breadth_first_search_2(graph, start):
    # return "came_from"
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from


def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start)  # optional
    path.reverse()  # optional
    return path


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        SquareGrid.__init__(self, width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return 1


def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far
