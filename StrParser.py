class Parser:
    def __init__(self, gui, brain):
        self.GUI = gui
        self.brain = brain
        self.brick_coordinates = []
        self.stone_coordinates = []
        self.water_coordinates = []
        self.player_name = "P0"

    def parse(self, data):
        # Game Start Message
        # S : P0;0,0;0 : P1;0,9;0 : P2;9,0;0 : P3;9,9;0 #
        if data[:2] == "S:":
            data = data[:-1]
            temp = data.split(":")
            no_of_players = len(temp) - 1
            tanks = []
            for i in range(len(temp)):
                if i != 0:
                    tank_info = temp[i].split(";")
                    name = tank_info[0]
                    x, y = tank_info[1][0], tank_info[1][2]
                    direction = tank_info[2]
                    tanks.append([name, x, y, direction])
            self.GUI.start(tanks)
            self.brain.addtanks(tanks)
            print tanks

        # Game Initialization
        # I: P2 : 2,1;8,6;0,8;2,4;7,1;9,3;1,8;7,4;2,6;4,8 : 0,3;5,7;1,4;3,6;7,6;1,3;7,2;6,8;6,3;2,7 : 7,8;0,4;5,8;1,7;9,8;4,7;4,2;4,3;6,2;2,3 #
        elif data[:2] == "I:":
            data = data[:-1]
            temp = data.split(":")
            self.player_name = int(temp[1][1])
            self.brick_coordinates = [(eval(x[0]), eval(x[2])) for x in temp[2].split(";")]
            self.stone_coordinates = [(eval(x[0]), eval(x[2])) for x in temp[3].split(";")]
            self.water_coordinates = [(eval(x[0]), eval(x[2])) for x in temp[4].split(";")]
            self.GUI.initGUI(self.brick_coordinates, self.stone_coordinates, self.water_coordinates)
            self.brain.initBrain(self.player_name, self.brick_coordinates, self.stone_coordinates, self.water_coordinates)
            print(self.player_name, self.brick_coordinates, self.stone_coordinates, self.water_coordinates)

        # Global Update
        # G:P0;0,0;1;0;100;0;0:P1;0,9;1;0;100;0;0:P2;9,0;0;0;100;0;0:P3;9,9;3;0;100;0;0:2,1,0;8,6,0;0,8,0;2,4,0;7,1,0;9,3,0;1,8,0;7,4,0;2,6,0;4,8,0#
        elif data[:2] == "G:":
            data = data[:-1]
            temp = data.split(":")
            player_info = []
            for i in range(1, len(temp) - 1):
                player_info.append([eval(each) for each in temp[i].split(";")[1:]])
            brick_health = [eval(each) for each in temp[-1].split(";")]
            # self.gui.update(player_info,brick_health)
            # self.GUI.initGUI(self.brick_coordinates, self.stone_coordinates, self.water_coordinates)
            self.brain.update(player_info)
            self.GUI.updatePlayers(player_info)

        # Coin Packs
        elif data[:2] == "C:":
            data = data[:-1]
            coin_detail = [eval(each) for each in data.split(":")[1:]]
            print coin_detail
            self.brain.addCoin(coin_detail)
            self.GUI.addCoin(coin_detail)

        # Life Packs
        elif data[:2] == "L:":
            data = data[:-1]
            life_detail = [eval(each) for each in data.split(":")[1:]]
            print life_detail
            self.GUI.addLife(life_detail)
            self.brain.addLife(life_detail)
        else:
            print "Error"
            print data
