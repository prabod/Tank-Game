from Queue import Queue
from Messenger import Messenger
from random import randint


class Brain:
    def __init__(self):
        self.data = Queue()
        self.MOVES = ["RIGHT#", "LEFT#", "UP#", "DOWN#", "SHOOT#"]

    def update(self,data):
        self.data.put(data)
        self.decide(data)
        print data

    def decide(self,data):
        move = self.MOVES[randint(0, 3)]
        #print move

        #Messenger().send(move, '192.168.8.100', 6000)