import Server
import Brain
import GUI
import StrParser
from Messenger import Messenger

SERVER_IP = '0.0.0.0'
SERVER_PORT = 7000

brain = Brain.Brain()
gui = GUI.GUI(10, 10)
parser = StrParser.Parser(gui, brain)
def initServer():
    Messenger().send("JOIN#", '192.168.8.101', 6000)
    server = Server.ServerListner(SERVER_IP, SERVER_PORT)
    server.registerComponent(parser)
    #server.registerComponent(gui)
    server.run()


initServer()