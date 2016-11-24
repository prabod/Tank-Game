import Server
import Brain
import GUI
import StrParser
SERVER_IP = '0.0.0.0'
SERVER_PORT = 7000

brain = Brain.Brain()
gui = GUI.GUI(10, 10)
parser = StrParser.Parser(gui, brain)
def initServer():
    server = Server.ServerListner(SERVER_IP, SERVER_PORT)
    server.registerComponent(parser)
    #server.registerComponent(gui)
    server.run()


initServer()