from Queue import Queue


class GUI:
    def __init__(self):
        self.data = Queue()

    def update(self,data):
        self.data.put(data)
        print data